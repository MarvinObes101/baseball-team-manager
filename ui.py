"""
User interface module for the Baseball Team Manager application.

This module handles all console input and output.
"""

from objects import POSITIONS

LINE = "=" * 64


def display_menu():
    """
    Display the main menu and list of valid positions.
    """
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
    """
    Prompt the user for a menu option.

    Returns:
        str: The selected menu option.
    """
    return input("Menu option: ").strip()


def get_int(prompt):
    """
    Prompt the user for an integer.

    Args:
        prompt (str): Input prompt message.

    Returns:
        int: A valid integer.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid integer. Please try again.")


def get_position(prompt):
    """
    Prompt the user for a valid baseball position.

    Args:
        prompt (str): Input prompt message.

    Returns:
        str: A valid position code.
    """
    while True:
        pos = input(prompt).strip().upper()
        if pos in POSITIONS:
            return pos
        print("Invalid position. Please try again.")


def get_player_number(prompt="Number: "):
    """
    Prompt the user for a lineup number.

    Args:
        prompt (str): Input prompt message.

    Returns:
        int: A valid integer lineup number.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid number. Please try again.")


def display_lineup(lineup):
    """
    Display all players in the lineup.

    Args:
        lineup: An iterable collection of Player objects.
    """
    print()
    print(f"{'Player':<22}{'POS':<5}{'AB':<6}{'H':<6}{'AVG'}")
    print("-" * 50)
    for i, player in enumerate(lineup, start=1):
        print(f"{i:<2} {player.name:<20}{player.position:<5}{player.at_bats:<6}{player.hits:<6}{player.average:.3f}")
    print()


def display_message(message):
    """
    Display a message to the user.

    Args:
        message (str): The message to display.
    """
    print(message)
    print()