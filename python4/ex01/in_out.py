def square(x: int | float) -> int | float:
    """Returns square of value"""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Returns value powered by itself"""
    return x ** x


def outer(x: int | float, function) -> object:
    """Applies function to value each time it is called"""
    count = 0

    def inner() -> float:
        """Inner function that applies function\
         to value each time it is called"""
        nonlocal count, x
        count += 1
        x = function(x)
        return x
    return inner
