# Baseball Team Manager

## Overview

The Baseball Team Manager application is a menu-driven program that allows users to manage a baseball lineup using persistent CSV storage.

This project was developed in three stages to demonstrate progression from procedural programming to object-oriented programming (OOP).

---

## Section 1 – Procedural Version

The first version of the program was implemented using procedural programming techniques.

### Characteristics:
- Players stored as list-of-lists.
- All logic implemented inside `main.py`.
- CSV file used for data persistence.
- Manual input validation.
- Fully functional features:
  - Display lineup
  - Add player
  - Remove player
  - Move player
  - Edit player position
  - Edit player statistics

This version focused on functionality and meeting core requirements.

---

## Section 2 – Refactored Procedural Version

The second stage improved the structure and readability of the procedural implementation.

### Improvements:
- Reduced duplicated validation code.
- Introduced helper functions.
- Improved program organization.
- Cleaner control flow.
- Better separation of logic inside `main.py`.

This version focused on improving maintainability and structure while keeping the procedural approach.

---

## Section 3 – Object-Oriented Version

The final stage converts the application into an object-oriented design.

### Enhancements:
- Introduced a `Player` class.
- Introduced a `Lineup` class with encapsulation.
- Implemented a custom iterator in `Lineup`.
- Separated responsibilities into modules.

### Module Responsibilities

| File | Responsibility |
|------|---------------|
| `objects.py` | Business logic (Player and Lineup classes) |
| `db.py` | CSV file reading and writing |
| `ui.py` | User input and output handling |
| `main.py` | Program coordinator |
| `players.csv` | Persistent player data |

This version demonstrates proper software architecture and object-oriented programming principles.

---

## Features

- Display lineup with batting average calculation
- Add new player with validation
- Remove player by lineup position
- Move player within lineup
- Edit player position
- Edit player statistics
- Persistent storage using CSV
- Custom iterator implementation

---

## API Documentation

### main.py

The `main.py` module acts as the main controller of the application.  
It coordinates communication between the user interface, the business objects, and the data storage layer.

#### validate_stats(at_bats, hits)

Validates a player's batting statistics.

Parameters:
- `at_bats (int)` – number of at-bats
- `hits (int)` – number of hits

Returns:
- `True` if the statistics are valid
- `False` if the statistics are invalid

Rules:
- At-bats must be greater than or equal to 0
- Hits must be greater than or equal to 0
- Hits cannot exceed at-bats

#### load_lineup()

Loads player data from the CSV file and initializes the lineup object.

Returns:
- `Lineup` object containing all players from the file

Process:
1. Reads players from `players.csv`
2. Creates a new `Lineup`
3. Adds each player to the lineup

#### main()

The main program loop that runs the application.

Responsibilities:
- Displays the menu
- Processes user commands
- Executes lineup operations
- Saves changes to the CSV file

Menu options handled:

| Option | Action |
|------|------|
| 1 | Display lineup |
| 2 | Add player |
| 3 | Remove player |
| 4 | Move player |
| 5 | Edit player position |
| 6 | Edit player statistics |
| 7 | Exit program |

---

### objects.py

Contains the core data classes used in the application.

#### Player Class

Represents a baseball player.

Attributes:
- `name`
- `position`
- `at_bats`
- `hits`

Property:
- `average` – calculates batting average.

#### Lineup Class

Manages a collection of Player objects.

Responsibilities:
- Add player
- Remove player
- Move player
- Update player position
- Update player statistics

Also implements a **custom iterator** to allow looping through players.

---

### db.py

Handles reading and writing player data to the CSV file.

Functions:
- `read_players()` – loads player data from `players.csv`
- `write_players(lineup)` – saves updated lineup to the CSV file

---

### ui.py

Handles all user input and output.

Key functions:
- `display_menu()` – displays menu options
- `display_lineup()` – prints formatted lineup table
- `get_int(prompt)` – validates integer input
- `get_position(prompt)` – validates position input
- `display_message()` – prints status messages

---

## File Structure


baseball-team-manager/
│
├── main.py
├── ui.py
├── objects.py
├── db.py
├── players.csv
└── README.md


---

## How to Run

1. Open the project folder in VS Code.
2. Open the terminal inside the project directory.
3. Run the program:


python main.py


---

## Technologies Used

- Python 3
- CSV module
- Dataclasses
- Object-Oriented Programming (OOP)
- Custom iterator implementation
- Git for version control
- GitHub for progress tracking

---

## Author

Marvin Ehiaguina