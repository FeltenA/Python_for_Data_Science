class calculator:
    """Calculator class"""

    def __init__(self, vect):
        """Calculator constructor"""
        self.vect = vect

    def __add__(self, object) -> None:
        """Addition of vector with a scalar"""
        self.vect = [x + object for x in self.vect]
        print(self.vect)

    def __mul__(self, object) -> None:
        """Multiplication of vector with a scalar"""
        self.vect = [x * object for x in self.vect]
        print(self.vect)

    def __sub__(self, object) -> None:
        """Substraction of vector with a scalar"""
        self.vect = [x - object for x in self.vect]
        print(self.vect)

    def __truediv__(self, object) -> None:
        """Division of vector with a scalar"""
        if (object == 0):
            raise ZeroDivisionError("division by zero")
        self.vect = [x / object for x in self.vect]
        print(self.vect)
