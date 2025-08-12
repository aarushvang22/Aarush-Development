from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "This is your home page."

@app.route("/counter")
def counter():
    text = request.args.get("text", "")
    text = text.strip()
    words = text.split(" ")
    counter = len(words)
    return f"There are {counter} words in this string."

if __name__ == "__main__":
    app.run()
