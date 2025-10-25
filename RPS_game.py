#ROCK PAPER AND SCISSOR GAME

#Importing random module 
import random


def choices(player_choice):
    
    cpu_choice = ["ROCK","PAPER","SCISSOR"]
    cpu_choice = random.choice(cpu_choice)   # store the random choice

    # if player chooses Paper 
    def for_PAPER():

        if player_choice == "PAPER" and cpu_choice == "ROCK":
            return(
                f"Your choice {player_choice}, CPU Choice {cpu_choice}\nSO PAPER covers ROCK, You win!!!"
                )
        
        #IF TIES TO REPLAY
        elif player_choice == "PAPER" and cpu_choice == "PAPER":
            print(
                f"Your choice {player_choice}, CPU Choice {cpu_choice}\nOOPS Match Tie!!!, Play Again--->"
                )
            return choices(input("Enter your choice (ROCK, PAPER, SCISSOR): ").upper())
        
        elif player_choice == "PAPER" and cpu_choice == "SCISSOR":
            return (
                f"Your choice {player_choice}, CPU Choice {cpu_choice}\nSO SCISSOR cuts PAPER, CPU win!!!"
                )


    # if player chooses Rock    
    def for_ROCK():

        #IF TIES TO REPLAY
        if player_choice == "ROCK" and cpu_choice == "ROCK":
            print(
                f"Your choice {player_choice}, CPU Choice {cpu_choice}\nOOPS Match Tie!!!, Play Again--->"
                )
            return choices(input("Enter your choice (ROCK, PAPER, SCISSOR): ").upper())

        elif player_choice == "ROCK" and cpu_choice == "PAPER":
            return (
                f"Your choice {player_choice}, CPU Choice {cpu_choice}\nSO PAPER covers ROCK, CPU win!!!"
                )
        
        elif player_choice == "ROCK" and cpu_choice == "SCISSOR":
            return (
                f"Your choice {player_choice}, CPU Choice {cpu_choice}\nSO ROCK breaks SCISSOR, You win!!!"
                )
        

    # if player chooses Scissor     
    def for_SCISSOR():
        if player_choice == "SCISSOR" and cpu_choice == "ROCK":
            return (
                f"Your choice {player_choice}, CPU Choice {cpu_choice}\nSO ROCK breaks SCISSOR, CPU wins!!!"
            )
        
        elif player_choice == "SCISSOR" and cpu_choice == "PAPER":
            return (
                f"Your choice {player_choice}, CPU Choice {cpu_choice}\nSO PAPER covers ROCK, You wins!!!"
            )        
        #IF TIES TO REPLAY
        elif player_choice == "SCISSOR" and cpu_choice == "SCISSOR":
            print(
                f"Your choice {player_choice}, CPU Choice {cpu_choice}\nSO OOPS Tie!!!, Play Again--->"
                )
            return choices(input("Enter your choice (ROCK, PAPER, SCISSOR): ").upper())



    # calling the correct function based on player's choice
    if player_choice == "PAPER":
        return for_PAPER()
    elif player_choice == "ROCK":
        return for_ROCK()
    elif player_choice == "SCISSOR":
        return for_SCISSOR()
    else:
        return "Invalid choice! TRY AGAIN",choices(input("Enter your choice (ROCK, PAPER, SCISSOR): ").upper())               #if player give invalid input

call = choices(input("Enter your choice (ROCK, PAPER, SCISSOR): ").upper())
print(call)                                   


    
