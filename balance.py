from db_utils import *
from lol_metadata import *


def toString(player):
    return "{} {}, {}{}".format(
        ranks[player["rank"]],
        player["div"],
        player["pos1"],
        "/ " + player["pos2"] if player["pos2"] != "" else "",
    )

def balance():
    players = get_all('players')
    players.sort(key=lambda p: ranks.index(p["rank"]) * 4 + int(p["div"]))
    subs = []
    teams = [{pos: "" for pos in positions} for _ in range(len(players) // 10 * 2)]
    for player in players:        
        player["rank"] += " " + str(player["div"])
        placed = False
        for team in teams:
            if team[player["pos1"]] == "":
                team[player["pos1"]] = player
                placed = True
                break
        if not placed:
            subs.append(player)

    # for team in teams:
    #     for pos, player in team.items():
    #         if player != "":
    #             print(
    #                 pos + ": " + toString(player),
    #                 end="| ",
    #             )
    #     print()

    # for player in left:
    #     print(toString(player))

    return teams, subs