import json
import os

from google import genai


def analyze_resume(resume_text, user_goal):
    prompt = f"""
You are a senior software engineer and hiring manager.
Evaluate the resume based on the user's goal.
User goal: "{user_goal}"

- Extract only relevant skills for this goal.
- Remove irrelevant tools.
- Identify real skill gaps.
- Generate a roadmap only for missing skills.
- Make the output specific to the user's goal.

Return only JSON:
{{
"skills": [],
"missing_skills": [],
"roadmap": [],
"interview_questions": []
}}
Resume:
{resume_text}
"""
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("Set GEMINI_API_KEY in your .env file to enable resume analysis.")

        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config={
                "temperature": 0.3,
                "response_mime_type": "application/json",
            },
        )
        if not response.text:
            raise ValueError("Gemini returned an empty response.")

        return json.loads(response.text)
    except Exception as error:
        return {
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "interview_questions": [],
            "error": str(error),
        }
