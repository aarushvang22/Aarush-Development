from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "This is your home page."

@app.route("/bmi")
def calculator():
    weight = request.args.get("weight", 0)
    height = request.args.get("height", 0)
    result = int(weight) / int(height)
    return f"BMI = {float(result)} kg/m squared"

if __name__ == "__main__":
    app.run()
