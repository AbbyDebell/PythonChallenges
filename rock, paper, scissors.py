player1 = input("please enter rock, paper or scissors ")
player2 = input("please enter rock, paper or scissors ")

if player1 == "rock" and player2 == "scissors" or player1 == "scissors" and player2 == "paper" or player1 == "paper" and player2 == "rock":
	print("player 1 wins!")
elif player2 == "rock" and player1 == "scissors" or player2 == "scissors" and player1 == "paper" or player2 == "paper" and player1 == "rock":
	print("player 2 wins!")
elif player1 == player2:
	print("It's a draw!")
else:
	print("Please choose between rock, paper or scissors")
	
# if player1 == "rock":
	# print("same")
# else:
	# print("no")
	