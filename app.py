import csv, random
import pandas as pd


def assign(row, teams):
    team_size = {x: len(y) for (x, y) in teams.items()}
    small = min(team_size.values())
    small_keys = [key for key in team_size if team_size[key] == small]
    new_team = random.choice(small_keys)
    teams[new_team].append(row["Name"])

    return teams


def export_teams(teams):
    df = pd.DataFrame({key: pd.Series(value) for key, value in teams.items()})
    df.to_csv("roster.csv")


def get_teams():
    teams = {}
    with open("characters.csv") as characters:
        reader = csv.reader(characters)
        for row in reader:
            teams[row[0]] = []

    return teams


def set_teams(teams):
    with open("names.csv") as names:
        reader = csv.DictReader(names)
        for row in reader:
            if row["Name"] == "Name":
                pass
            elif row["Character"] in teams.keys():
                teams[row["Character"]].append(row["Name"])
        names.seek(0)
        for row in reader:
            if row["Name"] == "Name":
                pass
            elif row["Character"] not in teams.keys():
                teams = assign(row, teams)
    return teams


if __name__ == "__main__":
    teams = get_teams()
    teams = set_teams(teams)
    export_teams(teams)
