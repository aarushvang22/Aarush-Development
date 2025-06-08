
# 🛒 Flask + SQLite Mini Project: Simple Product Catalog

## 🎯 Objective

Create a web application using **Flask** and **SQLite** that allows users to add products and view a catalog of all added products. Each product should have a name, category, and price.

---

## 🛠 Features to Implement

- A form to input a product's:
  - Name
  - Category
  - Price
- Save submitted product data into an SQLite database.
- Display a list of all saved products on a separate page.

---

## 📁 Folder Structure

```
simple_product_catalog/
├── app.py
├── templates/
│   ├── index.html
│   └── catalog.html
```

---

## 🧠 Concepts Covered

| Concept           | Purpose                                  |
|-------------------|-------------------------------------------|
| Flask Routing     | Create URLs for form and listing pages    |
| HTML Forms        | Collect product information               |
| SQLAlchemy ORM    | Interact with SQLite database             |
| Jinja2 Templates  | Display products dynamically              |

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
   - SQLAlchemy model for `Product`
   - Routes for home (form), adding product, and catalog view
2. HTML templates:
   - `index.html` for product entry
   - `catalog.html` to display saved products
3. Demonstration: Run the app and add at least 3 products, then display them.
