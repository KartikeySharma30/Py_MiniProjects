# Creating a most played Game -> ROCK | PAPER | SCISSORS 

import random


# Counting User Score and Computer Score for Tallying at the End
usw=0
comw=0

options = ["rock", "paper" , "scissors"]



# Taking User Inputs and Running the Game Upon Certain Conditions and Action made by the USER  
while True:
    uc=input(f"Enter Your Choice from {options} or q to quit :").lower()
    if(uc=='q'):
        break
    if(uc not in options):
        print("Enter Valid Choice")
        continue
    
    rn = random.randint(0,2)
    cc= options[rn]

    if uc == "rock" and cc == "scissors" :
        print (f"User Choice :{uc} | Computer Choice :{cc} ")
        print("You Won!!!")
        usw+=1
    elif uc == "scissors" and cc == "paper":
        print (f"User Choice :{uc} | Computer Choice :{cc} ")
        print("You Won!!!")
        usw+=1
    elif uc == "paper" and cc == "rock":
        print (f"User Choice :{uc} | Computer Choice :{cc} ")
        print("You Won!!!")
        usw+=1
    elif uc == cc:
        print (f"User Choice :{uc} | Computer Choice :{cc} ")
        print("Tie!!!")
    
    else:
        print (f"User Choice :{uc} | Computer Choice :{cc} ")
        print("Computer Won!!!")
        comw+=1

# Tallying the Total Score Of both USER and COMPUTER upon Quitting the Game 
print(f"User Score :{usw} | Computer Score :{comw}")