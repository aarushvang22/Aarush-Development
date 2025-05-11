# 📝 Student Report Card Generator using Flask

## 📚 Objective

Create a web-based **Student Report Card Generator** using **Python Flask** that allows users to enter student details and subject marks, calculates the total, percentage, and assigns a grade, and displays a formatted report card using HTML templates.

---

## 🛠️ Features to Implement

- Accept **student name**, **roll number**, and **marks** for 5 subjects.
- Calculate:
  - Total marks (out of 500)
  - Percentage
  - Grade based on percentage
- Display all entered and calculated data in a **report card layout**.
- Use **Jinja2 templates** to render HTML with dynamic data.

---

## 🎯 Core Flask Concepts Covered

| Concept                  | Implementation Example |
|--------------------------|------------------------|
| Routing                  | `/` for form, `/report` for result |
| URL Parameters (optional) | Can use `/report/<roll>` to view results later |
| Request and Response     | Use `request.form` to capture input |
| Forms                    | HTML form in `index.html` |
| Jinja2 Templates         | Render results dynamically in `report.html` |

---

## 🧮 Grade Calculation Logic

| Percentage | Grade |
|------------|-------|
| 90–100     | A+    |
| 80–89      | A     |
| 70–79      | B     |
| 60–69      | C     |
| 50–59      | D     |
| Below 50   | F     |

---

## 📁 Folder Structure

report_card_app/
├── app.py
├── templates/
│ ├── index.html
│ └── report.html