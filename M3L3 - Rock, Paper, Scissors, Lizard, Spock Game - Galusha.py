# Holden Galusha
# October 2, 2018
# M3L3 - Rock, Paper, Scissors, Lizard, Spock Game
# Pseudocode:
#	Import random module
#	Define dictionary w/ options for user to choose and their associated numerical values
#	Define five dictionaries, one for each option. Each option's dictionary contains that option's 2 possible victorious outcomes
#	Prompt user for input
#	Fetch numerical value of user's input
#	Have PC choose option
#	Print PC's choice
#	Fetch numerical value of PC's choice
#	Define function that accepts 2 arguments and determines victor
#	--Function pseudocode above functions--
#	Call initial function
#	Prompt user to exit

import random

options = {'Rock':1, 'Paper':2, 'Scissors':3, 'Lizard':4, 'Spock':5}

'''
These dictionaries represent the two possible victorious outcomes for each option.
Each outcome has an associated numerical value.
That value is determined by the sum of the associated values of the involved entities
For example,
	in the dictionary titled "options", 'Paper' has an associated value of 2.
	According to the dictionary called Paper, the two outcomes in which Paper would be victorious involve 'rock' and 'Spock', respectively.
	Rock's associated value is 1, and Spock's is 5, so:
	Paper (2) + Rock (1) = 3, and Paper (2) + Spock (5) = 7
	
There's probably a better way of making this game; however, when searching other solutions, none of them had the capability to print what the end scenario actually was.
They can only print who won.
'''
Rock = {5:'Rock crushes lizard', 4:'Rock crushes scissors'}
Paper = {3:'Paper covers rock', 7:'Paper disproves Spock'}
Scissors = {5:'Scissors cuts paper', 7:'Scissors decapitate lizard'}
Lizard = {9:'Lizard poisons Spock', 6:'Lizard eats paper'}
Spock = {8:'Spock smashes scissors', 6:'Spock vaporizes rock'}
	
#Display options for user, prompt for option input
user_choice = input("""
Select an option:
	Rock
	Paper
	Scissors
	Lizard
	Spock

>>>""")

#Make user's choice titlecase so it's found in options dictionary
user_choice = user_choice.title()
	
#Fetch the user's choice's associated numerical value
user_choice_number = options.get(user_choice)

#Computer chooses item from options dictionary
pc_choice = random.choice(list(options.keys()))	

#Tell user what the PC chose
print("PC CHOICE: "+pc_choice)

#Fetch PC's choice's associated numerical value
pc_choice_number = options.get(pc_choice)

'''
This function determines the victor.
The two arguments passed to it are user_choice and pc_choice.
determining_sum is the sum of the two choice's associated values
If the determining_sum is found in the dictionary that matches the user's choice, then its associated string is printed, thus informing the user of the outcome.
User is then alerted that he/she won

If the determining sum is not found in the user's choice's dictionary equivalent,
then the conditional moves on to the PC's choice's dictionary equivalent.
The determining_sum is then located in the dictionary, and its associated string is printed.
User is then alerted that the PC won.
''' 
def determine_victor(y, z):
	determining_sum = user_choice_number + pc_choice_number
	
	if determining_sum in eval(y).keys():
		print(eval(y).get(determining_sum))
		print("User wins.")
	else:
		print(eval(z).get(determining_sum))
		print("PC wins.")

			
'''
Determines if the game is a draw.
Checks if the user_choice == the pc_choice
If so, then the game is declared a draw
If not, then determine_victor() is called and the game proceeds
'''
def determine_if_draw(y, z):
	if y == z:
		print("User and PC chose the same option.\nThe game is a draw.")
	else:
		determine_victor(user_choice, pc_choice)
		
		
determine_if_draw(user_choice, pc_choice)

#Prompt user to exit
print("\n\nPress Enter to exit.")
input()
