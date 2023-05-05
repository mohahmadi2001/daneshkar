"""
module providing tak_raghami function
"""

def tak_raghami(number: int) -> int:
    """
    Implement the function to
    create single digit numbers
    """
    summing = 0
    while number !=0 :
        summing += number % 10
        number //= 10
        if summing > 9 and number == 0:
            number = summing
            summing = 0
    return summing

# print(tak_raghami(123456))

def sum_digits(number : int)->int:
    # summation = 0 
    # while number > 0:
    #     summation += number % 10
    #     number //= 10
    return sum(map(int,str(number)))

# print(sum_digits(123456))

digit = int(input())
# while digit > 9:
#     digit = sum_digits(digit)
# print(digit)

a = digit % 9
print(a if a!=0 else 9)