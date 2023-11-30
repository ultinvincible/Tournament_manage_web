import random
import string
from db_utils import *
from lol_metadata import *


def generate(count: int):
    ingames = []
    while len(ingames) < count:
        ingame = "".join(random.choices(string.ascii_letters, k=10))
        if ingame not in ingames:
            ingames.append(ingame)
    items = []
    for i in range(count):
        item = {
            "ingame": ingames[i],
            "fname": random.choice(string.ascii_uppercase)
            + "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 9))),
            "lname": random.choice(string.ascii_uppercase)
            + "".join(random.choices(string.ascii_lowercase, k=random.randint(4, 9))),
            "rank": random.choice(ranks),
            "div": random.randint(1, 4),
            "pos1": positions[i % len(positions)],
            "pos2": random.choice(positions),
        }
        if item["pos2"] == item["pos1"]:
            item["pos2"] = ""
        items.append(item)
    return items


def replace(collection_name, items: list):
    db['collection_name'].delete_many({})
    db['collection_name'].insert_many(items)


# def rename(collection, old_attr: str, new_attr: str):
#     items = collection.find()
#     for item in items:
#         value = item.pop(old_attr)
#         item[new_attr] = value
#         collection.replace_one({"_id": item["_id"]}, item)


items = generate(40)
replace('players', items)
