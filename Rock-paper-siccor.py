import random 


options = ["Rock", "Paper", "Scissor"]
winning_combinations  = {
    "Rock" : "Scissor",
    "Paper" : "Rock",
    "Scissor": "Paper"
}


computer_input = random.choice(options)

while True:
    user = input("Choose one of them Rock, Paper, Scissor or quit(exit): ")

    if user.lower() == 'exit':
        print("Thanks for playing the game, Good bye!")
        break

    if user not in options:
        print("Invalid choices")
        continue

    if user == computer_input:
        print('Tie')
        
    elif winning_combinations[user] == computer_input:
        print("You win") 

    else:
        print("Computer wins")
        
        

            
            



