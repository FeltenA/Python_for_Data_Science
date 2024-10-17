import sys

try:
    if len(sys.argv) < 2:
        exit(0)
    elif len(sys.argv) > 2:
        raise AssertionError("Incorrect number of arguments")
    try:
        nbr = int(sys.argv[1])
    except ValueError:
        raise AssertionError("Argument is not an integer")
except AssertionError as error:
    print(AssertionError.__name__ + ":", error)
    exit(0)

if nbr % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")