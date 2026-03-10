"""
Business objects for the Baseball Team Manager application.

This module defines the Player and Lineup classes used to store
and manage baseball lineup data.
"""

from dataclasses import dataclass

POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")


@dataclass
class Player:
    """
    Represents a baseball player.

    Attributes:
        name (str): The player's full name.
        position (str): The player's field position.
        at_bats (int): Total number of at-bats.
        hits (int): Total number of hits.
    """
    name: str
    position: str
    at_bats: int
    hits: int

    @property
    def average(self) -> float:
        """
        Calculate the player's batting average.

        Returns:
            float: Batting average rounded to 3 decimals.
        """
        if self.at_bats == 0:
            return 0.0
        return round(self.hits / self.at_bats, 3)


class Lineup:
    """
    Manages a collection of Player objects.

    The Lineup class supports adding, removing, moving, and updating
    players, and implements iteration over the player list.
    """

    def __init__(self):
        """
        Initialize an empty lineup.
        """
        self.__players = []
        self.__index = 0

    def add_player(self, player: Player):
        """
        Add a player to the lineup.

        Args:
            player (Player): The player to add.
        """
        self.__players.append(player)

    def remove_player(self, index: int):
        """
        Remove a player from the lineup by index.

        Args:
            index (int): Zero-based index of the player to remove.
        """
        self.__players.pop(index)

    def move_player(self, from_index: int, to_index: int):
        """
        Move a player from one lineup position to another.

        Args:
            from_index (int): Current zero-based index.
            to_index (int): New zero-based index.
        """
        player = self.__players.pop(from_index)
        self.__players.insert(to_index, player)

    def get_player(self, index: int) -> Player:
        """
        Get a player by index.

        Args:
            index (int): Zero-based player index.

        Returns:
            Player: The selected player.
        """
        return self.__players[index]

    def update_position(self, index: int, position: str):
        """
        Update a player's position.

        Args:
            index (int): Zero-based player index.
            position (str): New field position.
        """
        self.__players[index].position = position

    def update_stats(self, index: int, at_bats: int, hits: int):
        """
        Update a player's batting statistics.

        Args:
            index (int): Zero-based player index.
            at_bats (int): New at-bats value.
            hits (int): New hits value.
        """
        self.__players[index].at_bats = at_bats
        self.__players[index].hits = hits

    @property
    def count(self) -> int:
        """
        Get the number of players in the lineup.

        Returns:
            int: Total player count.
        """
        return len(self.__players)

    def __iter__(self):
        """
        Return the iterator object.

        Returns:
            Lineup: The lineup instance itself.
        """
        self.__index = 0
        return self

    def __next__(self):
        """
        Return the next player in the lineup.

        Returns:
            Player: The next player.

        Raises:
            StopIteration: When there are no more players.
        """
        if self.__index < len(self.__players):
            player = self.__players[self.__index]
            self.__index += 1
            return player
        raise StopIteration