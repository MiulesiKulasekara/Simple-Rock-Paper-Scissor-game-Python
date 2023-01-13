# Rock Paper Scissor game

import random

# Get key board inputs from user and computer

def getChoices():
    playerChoice = input("Enter your choice (Rock , Paper , Scissor) :")

    # List
    options = ["Rock" , "Paper" , "Scissor"] # List of options for the computer
    computerChoice = random.choice(options)

    # Dictioneries
    choices = {"player" : playerChoice , "computer" : computerChoice}

    return choices

# Check who is the winner

def checkWinner(player , computer):
    print("Your choice is "+player) # Concatenating Strings
    print(f"Computer choice is {computer}") # f-strings

    if player == computer:
        return "It is tie."
    elif player == "Rock":
        if computer == "Paper":
            return "Paper covers rock! You lose."
        else:
            return "Rock smashes scissor.You win."
    elif player == "Paper":
        if computer == "Scissor":
            return "Scissor cuts paper! You lose."
        else:
            return "Paper covers rock.You win."
    elif player == "Scissor":
        if computer == "Rock":
            return "Rock smashes scissor! You lose."
        else:
            return "Scissor cuts paper.You win."
    else:
        return "Error. Enter Rock , Paper or Scissor"
    
    
choicesFunction = getChoices()
checkFunction = checkWinner(choicesFunction["player"] , choicesFunction["computer"]) # accses dictioneries
print(checkFunction) # get result