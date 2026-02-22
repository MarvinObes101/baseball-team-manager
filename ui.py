# ui.py
# Contains ONLY input/output (printing and user input)

from objects import POSITIONS

LINE = "=" * 64


def display_menu():
    """Display the menu and valid positions."""
    print(LINE)
    print(" Baseball Team Manager")
    print(" MENU OPTIONS")
    print(" 1 - Display lineup")
    print(" 2 - Add player")
    print(" 3 - Remove player")
    print(" 4 - Move player")
    print(" 5 - Edit player position")
    print(" 6 - Edit player stats")
    print(" 7 - Exit program")
    print(" POSITIONS")
    print(", ".join(POSITIONS))
    print(LINE)


def get_menu_option():
    """Get the user's menu choice as a string."""
    return input("Menu option: ").strip()


def get_int(prompt):
    """Get a valid integer from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid integer. Please try again.")


def get_position(prompt):
    """Get a valid baseball position from the user."""
    while True:
        pos = input(prompt).strip().upper()
        if pos in POSITIONS:
            return pos
        print("Invalid position. Please try again.")


def get_player_number(prompt="Number: "):
    """Get a lineup number (1-based) from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid number. Please try again.")


def display_lineup(lineup):
    """Display the lineup (Lineup is iterable)."""
    print()
    print(f"{'Player':<22}{'POS':<5}{'AB':<6}{'H':<6}{'AVG'}")
    print("-" * 50)

    for i, player in enumerate(lineup, start=1):
        print(
            f"{i:<2} {player.name:<20}{player.position:<5}"
            f"{player.at_bats:<6}{player.hits:<6}{player.average:.3f}"
        )

    print()


def display_message(message):
    """Display a simple message."""
    print(message)
    print()