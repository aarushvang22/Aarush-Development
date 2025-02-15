from flask import Flask

app = Flask("Aarush")

@app.route("/")
def home():
    return "This is your home page."

@app.route("/biography")
def biography():
    return "I love reading books.\nI love playing video games.\nI love watching sports."

if __name__ == "__main__":
    app.run()