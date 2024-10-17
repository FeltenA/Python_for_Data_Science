def give_bmi(height: list[int | float], weight: list[int | float])\
 -> list[int | float]:
    """Takes a list of heights and a list of weights as arguments
    returns a list of the calculated bmi for each pair of height and weight"""

    try:
        if not isinstance(height, list) or not isinstance(weight, list)\
                or len(height) != len(weight)\
                or not all(isinstance(item, (int, float)) for item in height)\
                or not all(isinstance(item, (int, float)) for item in weight):
            raise AssertionError("Bad arguments")

        bmi = list()
        for i in range(len(height)):
            bmi.append(weight[i] / (height[i] ** 2))
    except (ZeroDivisionError, AssertionError):
        print("AssertionError: the arguments are bad")
        return []
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Takes a list of bmi and a limit as arguments and returns
    a list of booleans that shows which bmi is above the limit"""

    try:
        if not isinstance(bmi, list) or not isinstance(limit, int)\
                or not all(isinstance(item, (int, float)) for item in bmi):
            raise AssertionError("Bad arguments")
    except AssertionError:
        print("AssertionError: the arguments are bad")
        return []

    check = list()
    for item in bmi:
        check.append(True if item > limit else False)
    return check
