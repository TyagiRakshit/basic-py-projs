def add(*args):
    sum = 0 
    for nom in args:
        sum +=int(nom)
    return sum

def multiply(*args):
    product = 1
    for nom in args:
        product *= int(nom)
    return product

def subt(*args):
    if len(args) == 0:
        return 0
    result = int(args[0])
    for nom in args[1:]:
        result -= int(nom)
    return result

def divide(*args):
    if len(args) == 0:
        return 0
    result = int(args[0])
    for nom in args[1:]:
        if nom == 0:
            raise ValueError("Cannot divide by zero")
        result /= int(nom)
    return result