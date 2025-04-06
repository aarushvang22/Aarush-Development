from flask import Flask, request, redirect, url_for, render_template, session

app = Flask(__name__)

loginInformation = {"admin": "admin123", "aarush": "aarushlovescybersecurity", "aarav": "aaravlovesIT", "harsh": "harshlovescoding"}
@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in loginInformation and password == loginInformation[username]:
            #session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html")
    return render_template("login.html")
    
@app.route("/dashboard")
def dashboard():
    return "Successfully logged in!"

if __name__ == "__main__":
    app.run()