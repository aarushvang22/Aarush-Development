from flask import Flask, request

app = Flask("Word Counter")

@app.route("/")
def home():
    return "This is your home page."

@app.route("/counter")
def counter():
    text = request.args.get("text", "")
    words = text.split(" ")
    counter = len(words)
    for i in range(counter):
        numberOfWords = counter + i
        return f"There are {numberOfWords} words in this string."
        

if __name__ == "__main__":
    app.run()