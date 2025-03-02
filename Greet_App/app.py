import datetime
from flask import Flask, request

app = Flask("Greeting")

@app.route("/")
def home():
    return "This is your home page."

@app.route("/greeting/<name>")
def greeting(name):
    return f"Hello {name}"



# /greet?name=John

@app.route("/greetingWithParameters")
def greetingWithParameters():
    name = request.args.get("name", "Guest")
    return f"Hello {name}"

@app.route("/age/<birthYear>")
def age_calculator(birthYear):
    currentYear = datetime.datetime.now().year
    age = currentYear - int(birthYear)
    return f"You are {age} years old."

if __name__ == "__main__":
    app.run()