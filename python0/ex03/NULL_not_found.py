def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing: None <class 'NoneType'>")
    elif isinstance(object, float) and object != object:
        print("Cheese: nan <class 'float'>")
    elif isinstance(object, bool) and not object:
        print("Fake: False <class 'bool'>")
    elif isinstance(object, int) and object == 0:
        print("Zero: 0 <class 'int'>")
    elif isinstance(object, str) and not object:
        print("Empty: <class 'str'>")
    else:
        print("Type not found")
        return 1
    return 0