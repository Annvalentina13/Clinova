from flask import Flask, render_template, request, jsonify
from ai.gemini import generate_medical_summary
import os
import pdfplumber
import pytesseract
from PIL import Image

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from flask import send_file

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "uploads"

if not os.path.exists("uploads"):
    os.makedirs("uploads")


def extract_text(file_path):
    if file_path.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        return text

    else:
        img = Image.open(file_path)
        return pytesseract.image_to_string(img)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    age = request.form["age"]
    gender = request.form["gender"]
    symptoms = request.form["symptoms"]
    duration = request.form["duration"]
    history = request.form["history"]

    full_text = f"""
Age: {age}
Gender: {gender}
Symptoms: {symptoms}
Duration: {duration}
Medical History: {history}
"""

    if "report" in request.files:
        file = request.files["report"]
        if file.filename != "":
            path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(path)
            extracted = extract_text(path)
            full_text += "\nMedical Report:\n" + extracted

    ai_response = generate_medical_summary(full_text)

    return jsonify({"summary": ai_response})

@app.route("/download", methods=["POST"])
def download():
    summary = request.form["summary"]

    file_path = "doctor_report.pdf"
    c = canvas.Canvas(file_path, pagesize=letter)

    y = 750
    for line in summary.split("\n"):
        c.drawString(50, y, line)
        y -= 15

    c.save()

    return send_file(file_path, as_attachment=True)



if __name__ == "__main__":
    app.run(debug=True)
