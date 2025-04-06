from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "This is your home page."

@app.route("/generator", methods=["GET", "POST"])
def password_generator():
    password = ""
    if request.method == "POST":
        passwordLength = int(request.form.get("passwordLength", 8))
        for i in range(passwordLength):
            passwordNumberChoice = int(random.randint(1, 4))
            if passwordNumberChoice == 1:
                capitalLetters = int(random.randint(65, 90))
                character = chr(capitalLetters)
            elif passwordNumberChoice == 2:
                lowercaseLetters = int(random.randint(97, 122))
                character = chr(lowercaseLetters)
            elif passwordNumberChoice == 3:
                digits = int(random.randint(48, 57))
                character = chr(digits)
            else:
                specialCharacters = int(random.randint(33, 47))
                character = chr(specialCharacters)
            password += character
    return render_template("password.html", generatedPassword=password)

if __name__ == "__main__":
    app.run()
    