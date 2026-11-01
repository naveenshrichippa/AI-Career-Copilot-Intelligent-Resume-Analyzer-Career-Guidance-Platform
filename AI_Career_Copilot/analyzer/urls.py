from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", auth_views.LogoutView.as_view(),name="logout",),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("history/", views.history, name="history"),
]
