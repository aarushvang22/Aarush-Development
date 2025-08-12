from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "This is your home page."

@app.route("/converter")
def converter():
    temperature = request.args.get("temperature", type=float)
    unit = request.args.get("unit", "")
    if unit == "C":
        farenheitResult = (temperature * 9/5) + 32
        return f"{farenheitResult} degrees Farenheit"
    elif unit == "F":
        celsiusResult = (temperature - 32) * 5/9
        return f"{celsiusResult} degrees Celsius"
    else:
        return "Invalid Unit"

if __name__ == "__main__":
    app.run()
