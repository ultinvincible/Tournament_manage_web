from flask_pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017")

db = client["tournaments_data"]


def create_tournament(tournament_data: dict[str, str]):
    for key in ["players", "teams"]:
        tournament_data[key] = int(tournament_data[key])
    db["tournaments"].insert_one(tournament_data)


def get_all(collection: str):
    return list(db[collection].find())


def sign_up_player(player_data: dict[str, str]):
    db["players"].insert_one(player_data)
