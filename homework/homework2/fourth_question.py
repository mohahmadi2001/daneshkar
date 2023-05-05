"""
module providing factorial,power,my_round and neper function
"""
def factorial(number: int) -> int:
    """
    Implementation of factorial function
    """
    result = 1
    for i in range(1, number+1):
        result *= i
    return result

def power(base: int, exponent: int) -> int:
    """
    Implementation of power function
    """
    return base ** exponent

def my_round(number: int, digits: int) -> float:
    """
    Implementation of round function for setting Decimal Place range 
    """
    multiple = 10 ** digits
    return int(number * multiple) / multiple

def neper(numbers: int, exponent: int | float) -> float:
    """
    This function increases the number 
    of Neper to a power
    """
    result=0
    for number in range(numbers):
        result += power(exponent, number) /factorial(number)

    # return format(result,'.3f')
    # return round(result,3)
    # return f"{result: .3f}"
    return my_round(result , 3)

SERIES = neper(4,6.42)
print(SERIES)

