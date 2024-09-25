import random

code = []

while True:
    length = input("Give me the length of the code: ")
    while length in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
        result = int(length)
        
    if result < 0:
        for _ in range(result):
                print(random.randint(0, 9), end=" ")
        else:
            print("Please eif length.isdigit()nter a positive integer.")
    else:
        print("Give me a real number.")
        


