import random

code = []

code_len = input("Enter the length of the code: ")

if code_len.isdigit():
    code_len = int(code_len)

    for i in range (code_len):
        
        num = random.randint(0, 9)
        
        code.append(num)
        
    print("Your code is: ", end = "")
    for num in code:
        print(num, end = "")
        
else: 
    print("You dumb fuck")
        

    
        


