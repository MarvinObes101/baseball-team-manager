"""
Database access layer for the Baseball Team Manager application.

This module handles reading from and writing to the players.csv file.
"""

import csv
from objects import Player

FILENAME = "players.csv"


def read_players():
    """
    Read player data from the CSV file.

    Returns:
        list[Player]: A list of Player objects loaded from the file.
    """
    players = []
    with open(FILENAME, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                players.append(Player(row[0], row[1], int(row[2]), int(row[3])))
    return players


def write_players(lineup):
    """
    Write player data to the CSV file.

    Args:
        lineup: An iterable collection of Player objects.
    """
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for player in lineup:
            writer.writerow([player.name, player.position, player.at_bats, player.hits])