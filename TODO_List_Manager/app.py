from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return render_template("manager.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form["task"]
    tasks.append(task)
    return redirect(url_for('home'))

@app.route("/delete", methods=["POST"])
def delete():
    task = request.form["task"]
    tasks.pop(task)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run()