# -*- coding: utf-8 -*-
#%% Cell 1
print("*"*50)
print("Temperature Conversion Program")
print("*"*50)
print("This program converts from Fahrenheit to Celsius")

#%% Cell 2
# Prompt user for temperature
fahren = float(input("Give me the temperatur in fahrenheit: "))

# Convert temperature
cels = 5/9 * (fahren - 32)

# Display conversion
print(f"Your temperatur in celcius is {cels:.0f} Degrees Celsius.")