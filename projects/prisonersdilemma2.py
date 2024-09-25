print("*"*50)
print("Welcome to the prisoner's dilemma:")
print("*"*50)

print("Prisoner A, you're up!")
    
while True:
    
    choiceA = input("\nSelect 1 to confess and 2 to stay silent: ")
    
    if choiceA != "1" and choiceA != "2":
        
        print("\nInvalid input. Try again.")
        
    else:
        break
    
