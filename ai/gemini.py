import requests
import json
import os

API_KEY = os.getenv("AIzaSyAVoX0BQy6CVCxwVkEn4cYsqRMl-6Ywr3U")

URL = "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key=AIzaSyAVoX0BQy6CVCxwVkEn4cYsqRMl-6Ywr3U"

def generate_medical_summary(patient_text):

    prompt = f"""
You are a professional medical assistant helping a doctor.

Convert the following patient data into a structured, doctor-ready medical report.

Patient Information:
{patient_text}

Return in this format:

🧍 Patient Overview:
- Age:
- Gender:

🩺 Symptoms:
-

⏳ Duration:

📜 Medical History:

🧠 AI Analysis:
- Possible condition:
- Urgency level (Low/Medium/High):
- Reasoning:

🧪 Suggested Tests:

🚨 Red Flags:
"""

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    response = requests.post(URL, headers=headers, data=json.dumps(data))
    result = response.json()

    if "candidates" in result:
        return result["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return "Gemini API Error:\n" + str(result)
