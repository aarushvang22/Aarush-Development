from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///scoreboard.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Scoreboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(100))
    game = db.Column(db.String(100))
    score = db.Column(db.Integer)

@app.route("/")
def form():
    return render_template("index.html")

@app.route("/create", methods=["POST"])
def create_player_information():
    player_name = request.form["player_name"]
    game = request.form["game"]
    score = request.form["score"]
    player_data = Scoreboard(player_name=player_name, game=game, score=score)
    db.session.add(player_data)
    db.session.commit()
    return redirect("/view")

@app.route("/view")
def view_player_information():
    player_information = Scoreboard.query.all()
    return render_template("leaderboard.html", player_information=player_information)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()