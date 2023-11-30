from flask import Flask, render_template, request
from db_utils import *
from lol_metadata import *
from balance import balance

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/tournament_create")
def tournament_create():
    return render_template("tournament_create.html", formats=formats)


@app.route("/tournament_submit", methods=["POST"])
def tournament_submit():
    tournament = request.form.to_dict()
    create_tournament(tournament)
    return "Tournament created successfully!"


@app.route("/tournaments")
def tournaments():
    return render_template(
        "tournaments.html", items=get_all("tournaments"), labels=tournament_labels
    )


@app.route("/players")
def get_players():
    player_list = get_all("players")
    for player in player_list:
        player["rank"] += " " + str(player["div"])
    print(player_list)
    return render_template("players.html", items=player_list, labels=player_labels)


@app.route("/sign_up", methods=["GET"])
def sign_up():
    return render_template(
        "sign_up.html", ranks=ranks, divisions=divisions, positions=positions
    )


@app.route("/sign_up_submit", methods=["POST"])
def sign_up_submit():
    player = request.form.to_dict()
    sign_up_player(player)
    return "Sign up successful!"


@app.route("/teams")
def teams():
    teams, subs = balance()
    return render_template("teams.html", teams=teams, items=subs, labels=player_labels)


@app.route("/bracket")
def bracket():
    pass


if __name__ == "__main__":
    app.run()
