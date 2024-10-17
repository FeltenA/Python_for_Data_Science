import sys


def main():
    """Takes a string as argument and print the number of upper letters,
    lower letters, punctuation marks, spaces and digits"""

    try:
        if len(sys.argv) > 2:
            raise AssertionError("Too many arguments")
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        exit(0)

    if len(sys.argv) < 2 or not sys.argv[1]:
        print("What is the text to count?")
        msg = sys.stdin.readline()
    else:
        msg = sys.argv[1]

    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    print(f"The text contains {len(msg)} characters:")
    print(f"{sum(c.isupper() for c in msg)} upper letters")
    print(f"{sum(c.islower() for c in msg)} lower letters")
    print(f"{sum(c in punctuation for c in msg)} punctuation marks")
    print(f"{sum(c.isspace() for c in msg)} spaces")
    print(f"{sum(c.isdigit() for c in msg)} digits")


if __name__ == "__main__":
    main()
