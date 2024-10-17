from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive=True):
        """Constructor for the Baratheon family"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Makes the Baratheon character die"""
        self.is_alive = False

    def __str__(self) -> str:
        """Returns a string representation of the object"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Returns a string representation of the object"""
        return self.__str__()


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str, is_alive=True):
        """Constructor for the Lannister family"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @staticmethod
    def create_lannister(first_name: str, is_alive=True):
        """Create a Lannister"""
        return Lannister(first_name, is_alive)

    def die(self):
        """Makes the Lannister character die"""
        self.is_alive = False

    def __str__(self) -> str:
        """Returns a string representation of the object"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Returns a string representation of the object"""
        return self.__str__()
