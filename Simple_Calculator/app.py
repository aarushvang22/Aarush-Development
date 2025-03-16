from flask import Flask, request

app = Flask("Simple Calculator")

@app.route("/")
def home():
    return "This is the home page."

@app.route("/calculator")
def calculator():
    firstNumber = request.args.get("firstNumber", 0)
    secondNumber = request.args.get("secondNumber", 0)
    operation = request.args.get("operation", "").lower()
    if operation == "add":
        result = int(firstNumber) + int(secondNumber)
        return f"{int(firstNumber)} + {int(secondNumber)} = {result}"
    elif operation == "subtract":
        if int(firstNumber) > int(secondNumber):
            result = int(firstNumber) - int(secondNumber)
            return f"{int(firstNumber)} - {int(secondNumber)} = {result}"
        else:
            result = int(secondNumber) - int(firstNumber)
            return f"{int(secondNumber)} - {int(firstNumber)} = {result}"
    elif operation == "multiply":
        result = int(firstNumber) * int(secondNumber)
        return f"{int(firstNumber)} * {int(secondNumber)} = {result}"
    elif operation == "divide":
        if int(firstNumber) > int(secondNumber):
            result = int(firstNumber) / int(secondNumber)
            return f"{int(firstNumber)} / {int(secondNumber)} = {float(result)}"
        else:
            result = int(secondNumber) / int(firstNumber)
            return f"{int(secondNumber)} / {int(firstNumber)} = {float(result)}"
    else:
        return "Invalid Operation"

if __name__ == "__main__":
    app.run()