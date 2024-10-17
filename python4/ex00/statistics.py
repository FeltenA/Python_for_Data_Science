def ft_statistics(*args, **kwargs) -> None:
    """Prints the mean, the median, the quartile, the standard deviation
    and the variance of the received arguments
    according to the received kwargs"""
    largs = list(args)
    for op in kwargs.values():
        if op in ["mean", "median", "quartile", "std", "var"]:
            if not args or any(not isinstance(x, (int, float)) for x in args):
                print("ERROR")
                continue
            if op == "mean":
                print(f"mean : {sum(args) / len(args)}")
            elif op == "median":
                largs.sort()
                n = len(largs)
                if n % 2 == 0:
                    print("median : {}".format(
                        largs[n // 2 - 1] + largs[n // 2]) / 2)
                else:
                    print(f"median : {largs[n // 2]}")
            elif op == "quartile":
                largs.sort()
                n = len(largs)
                if n % 4 == 0:
                    fq = float((largs[n // 4] + largs[(n + 1) // 4]) / 2)
                else:
                    fq = float(largs[n // 4])
                if (3 * n) % 4 == 0:
                    tq = float(
                        (largs[3 * n // 4] + largs[(3 * (n + 1)) // 4]) / 2)
                else:
                    tq = float(largs[(3 * n) // 4])
                print(f"quartile : [{fq}, {tq}]")
            elif op == "std":
                mean = sum(largs) / len(largs)
                variance = sum([((x - mean) ** 2) for x in largs]) / len(largs)
                print(f"std : {variance ** 0.5}")
            elif op == "var":
                mean = sum(largs) / len(largs)
                variance = sum([((x - mean) ** 2) for x in largs]) / len(largs)
                print(f"var : {variance}")
