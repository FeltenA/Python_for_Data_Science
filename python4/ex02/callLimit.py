def callLimit(limit: int):
    """Decorator function to limit the call of a function"""
    count = 0

    def callLimiter(function):
        """Inner decorator function"""

        def limit_function(*args, **kwds):
            """Inner decorator function that checks for the limit"""
            nonlocal limit, count, function
            if limit > count:
                function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
            count += 1
        return limit_function
    return callLimiter
