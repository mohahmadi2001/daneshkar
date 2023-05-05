import math

def divide_numbers(num1: int | float , num2: int | float) -> float| None:
    """
    Divide num1 by num2 and return the result. If num2 is zero, return infinity.
    If num1 or num2 is not a number (NaN), return None.

    :param num1: The numerator
    :type num1: int | float
    :param num2: The denominator
    :type num2: int | float
    :return: The result of the division, or None if num1 or num2 is NaN.
    :rtype: float| None
    """
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return math.inf
    except TypeError:
        result = None
    else:
        if math.isnan(result):
            return None
    return result

print(divide_numbers(10, 2))
print(divide_numbers(6, 4)) 
print(divide_numbers(7, 3)) 
print(divide_numbers(9.3, 4)) 
print(divide_numbers(-6, 2)) 
print(divide_numbers(6, 0)) 
print(divide_numbers('reza', 4)) 
print(divide_numbers('reza', 'ali')) 