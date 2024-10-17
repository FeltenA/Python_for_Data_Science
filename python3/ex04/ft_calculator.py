class calculator:
    """Calculator class"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Prints dot product of two vectors"""
        res = 0
        for i in range(len(V1)):
            res += V1[i] * V2[i]
        print(f"Dot product is: {res}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Prints addition of two vectors"""
        res = []
        for i in range(len(V1)):
            res.append(float(V1[i] + V2[i]))
        print(f"Add Vector is : {res}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Prints subtraction of two vectors"""
        res = []
        for i in range(len(V1)):
            res.append(float(V1[i] - V2[i]))
        print(f"Sous Vector is: {res}")
