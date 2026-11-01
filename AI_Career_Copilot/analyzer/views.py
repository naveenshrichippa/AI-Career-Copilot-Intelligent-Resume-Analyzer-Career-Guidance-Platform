import docx
import PyPDF2

from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from ai import analyze_resume
from .forms import SignupForm
from .models import Report

User = get_user_model()


def home(request):
    return redirect("dashboard" if request.user.is_authenticated else "login")


def signup(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    form = SignupForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        User.objects.create_user(
            username=form.cleaned_data["email"],
            email=form.cleaned_data["email"],
            password=form.cleaned_data["password"],
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
        )
        messages.success(request, "Account created. You can now log in.")
        return redirect("login")

    return render(request, "signup.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password", "")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        messages.error(request, "Invalid email or password.")

    return render(request, "login.html")


@login_required
def dashboard(request):
    result = None

    if request.method == "POST":
        role = request.POST.get("role", "").strip()
        resume_text = request.POST.get("resume", "").strip()
        uploaded_file = request.FILES.get("file")

        if uploaded_file:
            filename = uploaded_file.name.lower()
            try:
                if filename.endswith(".pdf"):
                    reader = PyPDF2.PdfReader(uploaded_file)
                    resume_text = "".join(page.extract_text() or "" for page in reader.pages)
                elif filename.endswith(".docx"):
                    document = docx.Document(uploaded_file)
                    resume_text = "\n".join(paragraph.text for paragraph in document.paragraphs)
                else:
                    messages.error(request, "Upload a PDF or DOCX file.")
                    return render(request, "dashboard.html")
            except Exception as error:
                messages.error(request, f"Could not read the uploaded file: {error}")
                return render(request, "dashboard.html")

        if not role or not resume_text:
            messages.error(request, "Enter your career goal and provide resume text or a file.")
        else:
            result = analyze_resume(resume_text, role)
            Report.objects.create(
                user=request.user,
                role=role,
                resume_text=resume_text,
                result=result,
            )

    return render(request, "dashboard.html", {"result": result})


@login_required
def history(request):
    reports = Report.objects.filter(user=request.user)
    return render(request, "history.html", {"reports": reports})
