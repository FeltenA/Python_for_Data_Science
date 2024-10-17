import sys
from ft_filter import ft_filter


def main():
    """Takes two arguments a string(S) and an integer(N)
    outputs a list of words from S that have a length greater than N"""

    try:
        if len(sys.argv) != 3 or not isinstance(sys.argv[1], str):
            raise AssertionError()
        string = sys.argv[1]
        if any(not c.isalnum() and not c.isspace() for c in string):
            raise AssertionError()
        integer = int(sys.argv[2])
    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")
        exit(0)

    words = string.split()
    print(list(ft_filter(lambda x: len(x) > integer, words)))


if __name__ == "__main__":
    main()
