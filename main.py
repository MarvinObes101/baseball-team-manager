"""
main.py

Main controller for the Baseball Team Manager application.

This module coordinates the interaction between:
- ui.py for user interface operations
- db.py for reading and writing player data
- objects.py for Player and Lineup classes

The program loads players from the CSV file, allows the user
to manage the lineup through a menu-driven interface, and
saves updates back to the file.
"""

import db
import ui
from objects import Player, Lineup


def validate_stats(at_bats, hits):
    """
    Validate batting statistics.

    Args:
        at_bats (int): Number of at-bats.
        hits (int): Number of hits.

    Returns:
        bool: True if the statistics are valid, otherwise False.
    """
    return at_bats >= 0 and hits >= 0 and hits <= at_bats


def load_lineup():
    """
    Load players from the CSV file and create a Lineup object.

    Returns:
        Lineup: A lineup object populated with players.
    """
    players = db.read_players()
    lineup = Lineup()

    for player in players:
        lineup.add_player(player)

    return lineup


def main():
    """
    Main program loop.

    Displays the menu, processes user commands, and performs
    lineup operations such as adding, removing, moving, and
    editing players.
    """

    lineup = load_lineup()

    while True:
        ui.display_menu()
        choice = ui.get_menu_option()

        if choice == "1":
            ui.display_lineup(lineup)

        elif choice == "2":
            name = input("Name: ")
            pos = ui.get_position("Position: ")
            ab = ui.get_int("At bats: ")
            hits = ui.get_int("Hits: ")

            if not validate_stats(ab, hits):
                ui.display_message("Invalid stats. Hits must be 0..at_bats.")
                continue

            player = Player(name, pos, ab, hits)
            lineup.add_player(player)
            db.write_players(lineup)
            ui.display_message(f"{name} was added.")

        elif choice == "3":
            index = ui.get_player_number("Number: ") - 1
            player = lineup.get_player(index)
            lineup.remove_player(index)
            db.write_players(lineup)
            ui.display_message(f"{player.name} was removed.")

        elif choice == "4":
            current = ui.get_player_number("Current lineup number: ") - 1
            new = ui.get_player_number("New lineup number: ") - 1
            player = lineup.get_player(current)
            lineup.move_player(current, new)
            db.write_players(lineup)
            ui.display_message(f"{player.name} was moved.")

        elif choice == "5":
            index = ui.get_player_number("Number: ") - 1
            pos = ui.get_position("Position: ")
            player = lineup.get_player(index)
            lineup.update_position(index, pos)
            db.write_players(lineup)
            ui.display_message(f"{player.name} was updated.")

        elif choice == "6":
            index = ui.get_player_number("Number: ") - 1
            ab = ui.get_int("At bats: ")
            hits = ui.get_int("Hits: ")

            if not validate_stats(ab, hits):
                ui.display_message("Invalid stats. Hits must be 0..at_bats.")
                continue

            player = lineup.get_player(index)
            lineup.update_stats(index, ab, hits)
            db.write_players(lineup)
            ui.display_message(f"{player.name} was updated.")

        elif choice == "7":
            print("Bye!")
            break

        else:
            ui.display_message("Invalid menu option.")


if __name__ == "__main__":
    main()