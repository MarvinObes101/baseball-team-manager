# objects.py
# Contains the business logic (no input/print, no CSV reading/writing)

from dataclasses import dataclass

# Allowed positions (same as Section 2)
POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")


@dataclass
class Player:
    """Represents one player in the lineup."""
    name: str
    position: str
    at_bats: int
    hits: int

    @property
    def average(self) -> float:
        """Batting average rounded to 3 decimals. If at_bats is 0, avg is 0.0."""
        if self.at_bats == 0:
            return 0.0
        return round(self.hits / self.at_bats, 3)


class Lineup:
    """Manages a list of Player objects (encapsulated)."""

    def __init__(self):
        self.__players = []      # private list for encapsulation
        self.__index = 0         # used for iterator

    def add_player(self, player: Player):
        self.__players.append(player)

    def remove_player(self, index: int):
        self.__players.pop(index)

    def move_player(self, from_index: int, to_index: int):
        player = self.__players.pop(from_index)
        self.__players.insert(to_index, player)

    def get_player(self, index: int) -> Player:
        return self.__players[index]

    def update_position(self, index: int, position: str):
        self.__players[index].position = position

    def update_stats(self, index: int, at_bats: int, hits: int):
        self.__players[index].at_bats = at_bats
        self.__players[index].hits = hits

    @property
    def count(self) -> int:
        return len(self.__players)

    # Iterator support (so you can do: for p in lineup:)
    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index < len(self.__players):
            p = self.__players[self.__index]
            self.__index += 1
            return p
        raise StopIteration 