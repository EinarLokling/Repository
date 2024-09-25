print("This program will convert temperature from F/C") # Explaining the task
print("Enter 'F' for Fahrenheit to Celsius")
print("Enter 'C' for Celsius to Fahrenheit")

choice = input("Enter selection: ") # Getting input on F or C

if choice.upper() in ('F', 'C'): # Checking for a valid F or C input
    
    temp = input("Enter the temperature to convert: ") # Getting input on temperature
    
    try:
        temp = float(temp) # Converting temp to float for calculations
        
        if choice.upper() == "F": # If choice is Fahrenheit
            converted_temp = (temp-32) * 5/9
            print(f"{temp} in Fahrenheit is equal to {converted_temp:.1f} degrees Celsius.")
            
        else:
            converted_temp = 9/5 * (temp) - 32 # If choice is Celsius
            print(f"{temp} in Celsius is equal to {converted_temp:.1f} degrees Fahrenheit.")
            
    except: # If number input is not a number
        print("\nInvalid input!")
        print("You must enter a number")
        
else: # If temp input is not F or C
    print("\nInvalid input!")
    print("You can only press 'F' or 'C'")
