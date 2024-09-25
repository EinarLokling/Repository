import random

num1 = input("Give me lower bound: ") # Getting input, two numbers
num2 = input("Give me upper bound: ")

if num1.isdigit() and num2.isdigit(): # Checking if the input are numbers
    
    lower = int(num1) # The different inputs
    upper = int(num2)
    
    if lower<upper: # If the lower bound is lower than the upper bound
        rand_num = random.randint(lower, upper) # Creating the random number
        print(f"\nYou asked for a random number") # \n means jumping one line down
        print(f"Your random number is: {rand_num}") # Printing the random number
        
    else: # If the lower is higher than the upper
        print("\nEnter a valid upper bound (higher than the first number you dumbass)")
        
else: # If the input are not numbers
    print("\nEnter a valid number, you dumbass")
        
        
        