# Here in this Program we are generating random no. and adding untill a the MAX Score is not passed 
# but if the Player gets a 1 -> its score will be 0 other wise it will keep adding up

import random

# A Function reusable block of code
def roll(): 
    min_val=1
    max_val =6
    roll = random.randint(min_val,max_val)
    return roll
# Creating the no. of Players to compete -> by taking user input
while True :
    players = input("Enter the Number of players (2 - 4) :")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            break
        else:
            print("Must be b/w 2 - 4 players ")
    else:
        print("Invalid Try Again")

# MAX SCORE - > Can be made dynamic as well
max_score = 50 
player_score =[0 for _ in range(players)]



# Generating Random Score for playes and adding untill max Score is Reached or 1 is encountered
while max(player_score)<max_score:
    for pidx in range(players):
        print("\n"+f"Player :{pidx+1} Turn!")
        print(f"Your total score is :{player_score[pidx]}"+"\n")

        current_score =0

        while True:
            sr=input("Would you like to roll(y) :").lower()

            if sr!='y':
                break
            val=roll()
            if val==1:
                print("You roll a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score+=val
                print(f"You rolled a :{val}")

            print(f"Your score is :{current_score}")
        player_score[pidx]+=current_score
        print(f"Your total score is :{player_score[pidx]}")

# Main
max_score = max(player_score)
wind=player_score.index(max_score)
print(f"Player :{wind} won!!! with a Score of {max_score}")