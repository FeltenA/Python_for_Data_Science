def slice_me(family: list, start: int, end: int) -> list:
    """Takes a list as argument and slices it following
    the start and end arguments"""

    try:
        if not isinstance(family, list) or not isinstance(start, int) or\
                not isinstance(end, int) or\
                not all(isinstance(item, list) for item in family):
            raise AssertionError("Bad arguments")
        if not family:
            return []
        it = iter(family)
        l_len = len(next(it))
        if not all(len(item) == l_len for item in family):
            raise AssertionError("Bad arguments")
    except AssertionError:
        print("AssertionError: the arguments are bad")
        return []

    print(f"My shape is : ({len(family)}, {l_len})")
    new_family = family[start:end]
    print(f"My new shape is : ({len(new_family)}, {l_len})")
    return new_family
