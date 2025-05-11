from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("index.html")

@app.route("/report", methods=["POST"])
def result():
    student_name = request.form["student_name"]
    roll_number = int(request.form["roll_number"])
    math = int(request.form["math"])
    science = int(request.form["science"])
    english = int(request.form["english"])
    social_studies = int(request.form["social_studies"])
    IT = int(request.form["IT"])
    marks = math + science + english + social_studies + IT
    percentage_of_marks = marks / 5
    total_grade = calculate_grade(percentage_of_marks)
    return render_template("report.html", name=student_name, roll_number=roll_number, marks=marks, total_grade=total_grade, percentage=percentage_of_marks)

def calculate_grade(percentage_of_marks):
    if percentage_of_marks >= 90:
        return "A+"
    elif percentage_of_marks >= 80 and percentage_of_marks <= 89:
        return "A"
    elif percentage_of_marks >= 70 and percentage_of_marks <= 79:
        return "B"
    elif percentage_of_marks >= 60 and percentage_of_marks <= 69:
        return "C"
    elif percentage_of_marks >= 50 and percentage_of_marks <= 59:
        return "D"
    else:
        return "F"
    
if __name__ == "__main__":
    app.run()



