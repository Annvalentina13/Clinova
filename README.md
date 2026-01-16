#  Clinova
AI-Powered Clinical Pre-Screening & Triage System

Clinova is an intelligent healthcare platform that helps patients describe their symptoms and medical history, then uses Google Gemini AI to generate a structured, doctor-ready medical report — before the patient even meets a doctor.

---

## 🚨 Why Clinova?

Doctors spend a large portion of their time collecting basic patient information.  
Patients forget important symptoms, and emergencies are not detected early.

Clinova solves this by acting as an **AI medical intake assistant** that:
- Collects patient symptoms
- Analyzes uploaded reports
- Identifies possible conditions
- Flags urgent cases
- Generates a professional medical summary

---

## 🧠 What Clinova Does

1. Patient enters:
   - Age & Gender  
   - Symptoms (typed or spoken)  
   - Duration of symptoms  
   - Medical history  
   - Medical reports (PDF / images)

2. Clinova:
   - Extracts text from uploaded files (OCR + PDF parsing)
   - Sends everything to Google Gemini AI
   - Generates a structured clinical triage report

3. Doctor:
   - Views AI analysis
   - Sees possible diagnoses, urgency & red flags
   - Downloads a ready-to-use PDF report

---

## 📋 Example AI Output

Clinova generates:
- Patient overview
- Symptom summary
- Possible medical conditions
- Urgency level (Low / Medium / High)
- Suggested tests
- Red flags

This allows doctors to focus on **treatment**, not data collection.

---

## 🛠️ Tech Stack

| Layer | Technology |
|------|-----------|
Frontend | HTML, CSS, JavaScript |
Backend | Python, Flask |
AI Engine | Google Gemini 2.5 |
Speech | Web Speech API |
OCR | Tesseract + Pillow |
PDF Parsing | pdfplumber |
Report Export | ReportLab |

---

## 🚀 How to Run Clinova

1. Clone the repository  
```
git clone https://github.com/yourusername/clinova-ai

cd clinova-ai
```

2. Install dependencies  
```
pip install -r requirements.txt
```

3. Create `.env`  
```
GEMINI_API_KEY=YOUR_API_KEY
```

4. Run the app  
```
python app.py
```


5. Open  
```
http://127.0.0.1:5000
```
