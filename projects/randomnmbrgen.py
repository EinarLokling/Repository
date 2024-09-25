print("*"*50)
print("Welcome to the random number generator")
print("*"*50)


num1 = int(input("Give lower bound: "))
num2 = int(input("Give upper bound: "))

import random

if num1 > num2:
    print("du er dum")

if num2 >= num1:
    print(random.randint(num1, num2))