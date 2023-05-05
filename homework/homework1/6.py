# num1 , num2 = [int(x) for x in input().split()]

# prime_numbers = []
# for num in range(num1+1, num2):
#     if num <= 1:
#         continue
#     is_prime = True
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         prime_numbers.append(num)
# print(prime_numbers)

def is_prime(number):
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

# def prime(num1 , num2):
#     primes = []
#     for num in range(num1 +1, num2):
#         if is_prime(num):
#                 primes.append(num)
#     return primes

first = int(input())
second = int(input())
x= [i for i in range(first+1,second) if is_prime(i)]
print(*x,sep='-')