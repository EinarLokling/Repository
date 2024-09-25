# from "file" import "function"

from temp3 import tempConversion

def getScale():
    scale = input("Enter F or C: ")
    return scale

def getTemp():
    temp = float(input("Enter the temperature:"))
    return temp
                 

def main():
    
    print("*"*50)
    print("Welcome to the temperature convertion program")
    print("*"*50)
    
    scale = getScale()
    
    temp = getTemp()
    
    converted_temp = tempConversion(temp, scale)
    
    if scale == "F":
        print(f"{temp} degrees Fahrenheit is equal to {converted_temp:.2f} degrees Celsius.")
        
    else:
        print(f"{temp} degrees Celsius is equal to {converted_temp:.2f} degrees Fahrenheit.")


if __name__ == "__main__":
    
    main()

    