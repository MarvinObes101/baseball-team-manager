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

def main():
    while True:
        display_menu()
        choice = input("Menu option: ")

        if choice == "7":
            print("Bye!")
            break
        else:
            print("Feature not added yet.\n")

if __name__ == "__main__":
    main()
