from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///product.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(100))
    category = db.Column(db.String(100))
    price = db.Column(db.Integer)

@app.route("/")
def form():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_product():
    product = request.form["product"]
    category = request.form["category"]
    price = request.form["price"]
    new_product = Product(product=product, category=category, price=price)
    db.session.add(new_product)
    db.session.commit()
    return redirect("/view")

@app.route("/view")
def view_catalog():
    products = Product.query.all()
    return render_template("catalog.html", products=products)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()