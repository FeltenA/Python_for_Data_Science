import sys


def main():
    """Takes a string as argument and encodes it into morse code"""

    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
        "0": "----- "
    }

    try:
        if len(sys.argv) != 2 or not isinstance(sys.argv[1], str):
            raise AssertionError()
        string = sys.argv[1]
        if any(not c.isalnum() and not c == ' ' for c in string):
            raise AssertionError()
    except AssertionError:
        print("AssertionError: the arguments are bad")
        exit(0)

    for key in NESTED_MORSE.keys():
        string = string.upper().replace(key, NESTED_MORSE[key])
    print(string.rstrip())


if __name__ == "__main__":
    main()
