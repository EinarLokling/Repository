print("*"*50)
print("Welcome to the prisoner's dilemma:")
print("*"*50)

d = {
    "1" : "confess",
    "2" : "stay silent"
    }

choiceA = input('\nPrisoner A, you are up: \nPress 1 for "confess", press 2 for "stay silent": ')
choiceB = input('\nPrisoner B, you are up: \nPress 1 for "confess", press 2 for "stay silent": ')

if choiceA in d.keys() and choiceB in d.keys():
    print(f"\nPrisoner A chose to {d[choiceA]} and Prisoner B chose to {d[choiceB]}")
    
    if choiceA == "1" and choiceB == "1":
        print("You both get 2 years")
        
    elif choiceA == "1" and choiceB == "2":
        print("Prisoner A gets out now, Prisoner B gets 3 years")   
    
    elif choiceA == "2" and choiceB == "1":
        print("Prisoner A gets 3 years, Prisoner B gets out now")
        
    elif choiceA == "2" and choiceB == "2":
        print("You both get 1 year")
        
else:
    print("\nInvalid inputs!")
    print("You can only choose '1' or '2'")
