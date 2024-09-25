def getNum():
    
    num = float(input("Give me the number you want to exponentiate: "))
    base = float(input(f"Give me the number you want to exponentiate {num} with: "))
    
    return num, base

def exp(num, base):
    res = num ** base
    return res

def main(): # "main" takes no inputs
    
    # Define local variables
    num, base = getNum()

    # Function call to "exp"
    res = exp(num, base) 

    # Print result
    print(f'{num}^{base} = {res:.2f}')
    
    
