# computer guess
# this program can guess number from user

import random

# determine low limit and upper limit
low = 1
high = int(input("Enter the upper limit  : "))

program = True
while program:
    # guess number use random.randint()
    guess_number = random.randint(low,high) 
    print(f"\nGuess number : {guess_number}\n")
    
    while True:
        answer = input("Is the number too low (l), too high (h) or correct (c)  : ")
        if answer == "l":
            low = guess_number+1 # this is new lower limit
            break
        if answer == "h":
            high = guess_number-1 # this is new upper limit
            break
        if answer == "c":
            print(f"The guess number is correct, the number is {guess_number}")
            program = False
            break
        else:
            print(f"Guess number is {guess_number}")
            print("Please input (l), (h), or (c)\n")
            
                
