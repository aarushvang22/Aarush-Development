
# 📝 Flask + SQLite Mini Project: Name Saver App

## 🎯 Objective

Build a very simple web application using **Flask** and **SQLite** where users can enter their name, and view a list of all saved names.

---

## 🛠 Features to Implement

- A form to input a name.
- Save submitted names into an SQLite database.
- Display a list of all saved names on a separate page.

---

## 📁 Folder Structure

```
simple_db_app/
├── app.py
├── templates/
│   ├── index.html
│   └── names.html
```

---

## 🧠 Concepts Covered

| Concept           | Purpose                                  |
|-------------------|-------------------------------------------|
| Flask Routing     | Create URLs for viewing and submitting    |
| HTML Forms        | Collect user input                        |
| SQLAlchemy ORM    | Interact with SQLite database             |
| Jinja2 Templates  | Display dynamic content                   |

---

## 🔧 Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy

Install dependencies using:

```bash
pip install flask flask_sqlalchemy
```

---

## ✅ Deliverables

1. `app.py` with:
   - Database model
   - Routes for form, insert, and view
2. HTML templates:
   - `index.html` for form
   - `names.html` to show saved names
3. Demonstration: run the app and add at least 3 names, then display them.

---

## 📌 Extra Credit (Optional)

- Allow deleting a name from the list.
- Add timestamps for when each name was added.
- Style the page using basic CSS or Bootstrap.
