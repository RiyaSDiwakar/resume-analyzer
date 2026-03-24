from flask import Flask, render_template, request
from modules.parser import extract_text
from modules.analyzer import analyze_resume

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files["resume"]
    jd_text = request.form["jd"]
    
    resume_text = extract_text(file)
    results = analyze_resume(resume_text, jd_text)
    
    return render_template("result.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)