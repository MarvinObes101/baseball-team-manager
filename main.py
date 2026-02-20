import db

# Constants
POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")
LINE = "=" * 64


def display_menu():
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


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid integer. Please try again.")


def get_position(prompt):
    while True:
        pos = input(prompt).strip().upper()
        if pos in POSITIONS:
            return pos
        print("Invalid position. Please try again.")


def calc_avg(at_bats, hits):
    if at_bats == 0:
        return 0.0
    return round(hits / at_bats, 3)


def display_lineup(players):
    print()
    print(f"{'Player':<22}{'POS':<5}{'AB':<6}{'H':<6}{'AVG'}")
    print("-" * 50)
    for i, p in enumerate(players, start=1):
        name = p[0]
        pos = p[1]
        ab = int(p[2])
        hits = int(p[3])
        avg = calc_avg(ab, hits)
        print(f"{i:<2} {name:<20}{pos:<5}{ab:<6}{hits:<6}{avg:.3f}")
    print()


def add_player(players):
    name = input("Name: ").strip()
    pos = get_position("Position: ")
    ab = get_int("At bats: ")
    hits = get_int("Hits: ")

    if ab < 0 or hits < 0 or hits > ab:
        print("Invalid stats. Hits must be 0..at_bats and values can't be negative.\n")
        return

    players.append([name, pos, str(ab), str(hits)])
    db.write_players(players)
    print(f"{name} was added.\n")

def remove_player(players):
    try:
        number = int(input("Number: "))
    except ValueError:
        print("Invalid number.\n")
        return

    index = number - 1

    if index < 0 or index >= len(players):
        print("Invalid lineup number.\n")
        return

    name = players[index][0]
    players.pop(index)
    db.write_players(players)

    print(f"{name} was removed.\n")

def move_player(players):
    # Get current lineup number
    try:
        current_num = int(input("Current lineup number: "))
    except ValueError:
        print("Invalid number.\n")
        return

    current_index = current_num - 1

    # Validate current index
    if current_index < 0 or current_index >= len(players):
        print("Invalid lineup number.\n")
        return

    name = players[current_index][0]
    print(f"{name} was selected.")

    # Get new lineup number
    try:
        new_num = int(input("New lineup number: "))
    except ValueError:
        print("Invalid number.\n")
        return

    new_index = new_num - 1

    # Validate new index
    if new_index < 0 or new_index >= len(players):
        print("Invalid lineup number.\n")
        return

    # Move the player
    player = players.pop(current_index)
    players.insert(new_index, player)

    # Save changes
    db.write_players(players)

    print(f"{name} was moved.\n")

def edit_player_position(players):
    # Get lineup number
    try:
        number = int(input("Number: "))
    except ValueError:
        print("Invalid number.\n")
        return

    index = number - 1

    # Validate lineup number
    if index < 0 or index >= len(players):
        print("Invalid lineup number.\n")
        return

    # Show selected player
    name = players[index][0]
    print(f"{name} was selected.")

    # Get and validate new position
    pos = get_position("Position: ")

    # Update position (players row format: [name, pos, ab, hits])
    players[index][1] = pos

    # Save changes
    db.write_players(players)

    print(f"{name} was updated.\n")            

def main():
    players = db.read_players()

    while True:
        display_menu()
        choice = input("Menu option: ").strip()

        if choice == "1":
            display_lineup(players)
        elif choice == "2":
            add_player(players)
        elif choice == "3":
            remove_player(players)
        elif choice == "4":
            move_player(players)
        elif choice == "5":
            edit_player_position(players)             
        elif choice == "7":
            print("Bye!")
            break
        else:
            print("Feature not added yet.\n")


if __name__ == "__main__":
    main()
