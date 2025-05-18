from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///people.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

@app.route("/")
def render():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    new_person = Person(name=name)
    db.session.add(new_person)
    db.session.commit()
    return redirect("/names")


@app.route("/names")
def names():
    people = Person.query.all()
    return render_template("names.html", people=people)

if __name__ == "__main__":
    with app.app_context():
        db.create_all() #Create DB table on first run
    app.run()