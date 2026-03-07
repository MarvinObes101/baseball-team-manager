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