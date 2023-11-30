import math
import random
from itertools import combinations


def generate(teams: list, format: int):
    methods = [
        generate_single_elimination,
        generate_double_elimination,
        generate_single_round_robin,
        generate_double_round_robin,
    ]
    if format >= len(methods):
        print("Invalid format")
    else:
        methods[format](teams)


def generate_single_elimination(teams: list):
    num_rounds = int(math.log2(len(teams)))
    bracket = [[] for _ in range(num_rounds + 1)]

    random.shuffle(teams)

    for i, team in enumerate(teams):
        bracket[0].append(team)

    for round_num in range(1, num_rounds + 1):
        num_matches = 2 ** (num_rounds - round_num)
        for match_num in range(num_matches):
            bracket[round_num].append(None)

    return bracket



def generate_double_elimination(teams: list):
    num_rounds = int(math.log2(len(teams))) + 1
    bracket = [[] for _ in range(num_rounds)]

    num_matches = len(teams) // 2
    for i in range(num_matches):
        match = [teams[i * 2], teams[i * 2 + 1]]
        bracket[0].append(match)

    for round_num in range(1, num_rounds):
        num_matches = math.ceil(num_matches / 2)
        for i in range(num_matches):
            match = [None, None]
            bracket[round_num].append(match)

    return bracket


def generate_single_round_robin(teams: list):
    num_rounds = len(teams) - 1
    schedule = [[] for _ in range(num_rounds)]

    for round_num in range(num_rounds):
        schedule[round_num] = list(combinations(teams, 2))
        teams.insert(1, teams.pop())

    return schedule


def generate_double_round_robin(teams: list):
    return generate_single_round_robin(teams) + generate_single_round_robin(teams)


teams4 = ["Team 1", "Team 2", "Team 3", "Team 4"]

print("single_round_robin")
schedule = generate_single_round_robin(teams4)
for round_num, matches in enumerate(schedule):
    print("Round", round_num + 1)
    for match in matches:
        print(match[0], "vs", match[1])
    print()

print("double_round_robin")
schedule = generate_double_round_robin(teams4)
for round_num, matches in enumerate(schedule):
    print("Round", round_num + 1)
    for match in matches:
        print(match[0], "vs", match[1])
    print()

teams8 = [
    "Team 1",
    "Team 2",
    "Team 3",
    "Team 4",
    "Team 5",
    "Team 6",
    "Team 7",
    "Team 8",
]

print("single_elimination")
bracket = generate_single_elimination(teams8)
for round_num, matches in enumerate(bracket):
    print("Round", round_num + 1)
    for match in matches:
        print(match[0], "vs", match[1])
    print()

print("double_elimination")
bracket = generate_double_elimination(teams8)
for round_num, matches in enumerate(bracket):
    print("Round", round_num + 1)
    for match in matches:
        print(match[0], "vs", match[1])
    print()
