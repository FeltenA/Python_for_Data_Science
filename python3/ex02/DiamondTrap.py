from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the king."""

    def __init__(self, first_name: str, is_alive=True):
        """Constructor for the king"""
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        """Get the eyes of the king"""
        return self.eyes

    def set_eyes(self, value):
        """Set the eyes of the king"""
        if not isinstance(value, str):
            raise ValueError("Eyes need to be a string")
        self.eyes = value

    def get_hairs(self):
        """Get the hairs of the king"""
        return self.hairs

    def set_hairs(self, value):
        """Set the hairs of the king"""
        if not isinstance(value, str):
            raise ValueError("Hairs need to be a string")
        self.hairs = value
