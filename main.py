import db
import ui
from objects import Player, Lineup, POSITIONS


def validate_stats(at_bats, hits):
    """Return True if stats are valid, otherwise False."""
    return at_bats >= 0 and hits >= 0 and hits <= at_bats


def get_valid_index(lineup, prompt="Number: "):
    """
    Get a 0-based index for the lineup.
    Returns None if invalid.
    """
    number = ui.get_player_number(prompt)
    index = number - 1

    if index < 0 or index >= lineup.count:
        ui.display_message("Invalid lineup number.")
        return None

    return index


def add_player(lineup):
    """Handle menu option 2: add player."""
    name = input("Name: ").strip()  # keeping simple like Section 1/2
    position = ui.get_position("Position: ")
    at_bats = ui.get_int("At bats: ")
    hits = ui.get_int("Hits: ")

    if not validate_stats(at_bats, hits):
        ui.display_message("Invalid stats. Hits must be 0..at_bats and values can't be negative.")
        return

    lineup.add_player(Player(name, position, at_bats, hits))
    db.write_players(lineup)
    ui.display_message(f"{name} was added.")


def remove_player(lineup):
    """Handle menu option 3: remove player."""
    index = get_valid_index(lineup)
    if index is None:
        return

    name = lineup.get_player(index).name
    lineup.remove_player(index)
    db.write_players(lineup)
    ui.display_message(f"{name} was removed.")


def move_player(lineup):
    """Handle menu option 4: move player."""
    current_index = get_valid_index(lineup, "Current lineup number: ")
    if current_index is None:
        return

    name = lineup.get_player(current_index).name
    ui.display_message(f"{name} was selected.")

    new_index = get_valid_index(lineup, "New lineup number: ")
    if new_index is None:
        return

    lineup.move_player(current_index, new_index)
    db.write_players(lineup)
    ui.display_message(f"{name} was moved.")


def edit_player_position(lineup):
    """Handle menu option 5: edit position."""
    index = get_valid_index(lineup)
    if index is None:
        return

    player = lineup.get_player(index)
    ui.display_message(f"{player.name} was selected.")

    position = ui.get_position("Position: ")
    lineup.update_position(index, position)
    db.write_players(lineup)
    ui.display_message(f"{player.name} was updated.")


def edit_player_stats(lineup):
    """Handle menu option 6: edit stats."""
    index = get_valid_index(lineup)
    if index is None:
        return

    player = lineup.get_player(index)
    ui.display_message(f"{player.name} was selected.")

    at_bats = ui.get_int("At bats: ")
    hits = ui.get_int("Hits: ")

    if not validate_stats(at_bats, hits):
        ui.display_message("Invalid stats. Hits must be 0..at_bats and values can't be negative.")
        return

    lineup.update_stats(index, at_bats, hits)
    db.write_players(lineup)
    ui.display_message(f"{player.name} was updated.")


def main():
    # Load Player objects from CSV
    players = db.read_players()

    # Put them into a Lineup object
    lineup = Lineup()
    for p in players:
        lineup.add_player(p)

    while True:
        ui.display_menu()
        choice = ui.get_menu_option()

        if choice == "1":
            ui.display_lineup(lineup)
        elif choice == "2":
            add_player(lineup)
        elif choice == "3":
            remove_player(lineup)
        elif choice == "4":
            move_player(lineup)
        elif choice == "5":
            edit_player_position(lineup)
        elif choice == "6":
            edit_player_stats(lineup)
        elif choice == "7":
            ui.display_message("Bye!")
            break
        else:
            ui.display_message("Invalid menu option. Please try again.")


if __name__ == "__main__":
    main()