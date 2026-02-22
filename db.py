import csv
from objects import Player

FILENAME = "players.csv"


def read_players():
    """
    Reads players.csv and returns a list of Player objects.
    CSV format per row: name, position, at_bats, hits
    """
    players = []

    with open(FILENAME, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            # Skip blank rows
            if not row:
                continue

            # row: [name, position, at_bats, hits]
            name = row[0].strip()
            position = row[1].strip().upper()
            at_bats = int(row[2])
            hits = int(row[3])

            players.append(Player(name, position, at_bats, hits))

    return players


def write_players(lineup):
    """
    Writes Player objects back to players.csv.
    Accepts either:
      - a Lineup object (iterable), or
      - a list of Player objects
    """
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        for player in lineup:
            writer.writerow([player.name, player.position, player.at_bats, player.hits])