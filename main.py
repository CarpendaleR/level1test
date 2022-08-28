# Level 1 project
# Raymond
# august 22

# -Instructions
# -Variables and lists

# – declare the winner (toa), for example, ‘You chose 1, I chose 3, the total is 4. You are odds
# ‘username’, you lose.’

# • if the number of wins of the user is more than the number of wins by the computer, tell the
# user they have won a reward of their choice from a list
# • show the list of prizes. Possible gifts include iPhone, car, mountain bike, money, overseas
# trip, movie tickets, motorbike and Westfield vouchers
# • choose a random number to decide which prize has been won
# • tell the user what they have won.
import random

name_first = input("Your name?")
instructions = input("Do you know how to play? y/n").lower().strip()
odd_or_even = input("odd or even").lower().strip()
number_of_rounds = int(input("Number of rounds?"))
lower_range = int(input("Lower #"))
upper_range = int(input("Upper #"))

print(f"Sup {name_first}")
# Game loop
rounds_won = 0
rounds_lost = 0
game_result_list = []
i = 1
while i <= number_of_rounds:
    number_choice = int(input("Choose number"))
    computer_number = random.randrange(lower_range, upper_range)
    total_number = number_choice + computer_number
    if total_number % 2 == 0:
        winner = name_first
        rounds_won += 1
    else:
        winner = "Computer"
        rounds_lost += 1
    print(f"You chose {number_choice}, "
          f"I chose {computer_number}, "
          f"the total number is {total_number}. "
          f"You are {odd_or_even} {name_first}, "
          f"you win/lose.")
    game_result_list.append(winner)
    i += 1

# Print out the game summaries from list and announce the winner
print(f"Results of the {number_of_rounds} games")
i = 0
while i < number_of_rounds:
    print(f"Round {i+1} was won by {game_result_list[i]}")
    i += 1
print(f"{name_first} won {rounds_won} and the Computer won {rounds_lost}.")
if rounds_won > rounds_lost:
    print(f"{name_first} is the winner!")
else:
    print(f"The computer got you this time {name_first}, better luck next time")
print(f"Thanks for playing.")
