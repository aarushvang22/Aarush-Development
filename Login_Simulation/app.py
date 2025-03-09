from flask import Flask, request

app = Flask("Login Simulation")


users = {
    "admin": "12345678",
    "Harsh": "password456"
}


@app.route("/")
def home():
    return "This is your home page."

@app.route("/login")
def login():
    username = request.args.get("username", "")
    password = request.args.get("password", "")
    if username != "" and password != "":
        if username in users and users[username] == password:
            return "You are logged in!"
        else:
            return "Incorrect username of password! Try again!"
    else:
        print("Missing username and/or password")

if __name__ == "__main__":
    app.run()