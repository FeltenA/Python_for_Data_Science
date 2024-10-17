from abc import ABC, abstractmethod


class Character(ABC):
    """Character class"""

    def __init__(self, first_name: str, is_alive=True):
        """Character constructor"""
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        if not isinstance(is_alive, bool):
            raise TypeError("is_alive must be a boolean")
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract die class"""
        pass


class Stark(Character):
    """Representing the Stark family."""

    def die(self):
        """Makes the Stark character die"""
        self.is_alive = False
