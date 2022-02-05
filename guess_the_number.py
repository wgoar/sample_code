#Number Guessing Game Objectives:
import random
from guess_the_number_art import logo
# Include an ASCII art logo.
print(logo)
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

###Global Constants####
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

###Functions################
def compare_values(guess, random_number, turns):
  """Checks the randome number against the guess. Returns the number of turns remaining. """
  if guess > random_number:
    print ("Too high")
    return turns-1
  elif guess < random_number:
    print ("Too Low")
    return turns-1
  else:
    print (f"Correct! The number was {random_number}.")

def difficulty():
  choice = input("Choose a difficulty. Type 'easy' or 'hard': ") 
  if choice == "easy":
    #print ("You have 10 attempts remaining to guess the correct number.")
    return EASY_LEVEL_TURNS
  elif choice == "hard":
    #print("You have 5 attempts remaining to guess the correct number.")
    return HARD_LEVEL_TURNS
  else:
    raise ValueError(choice)
    print("That is not an option.")

def game():
  print("Welcome to the Number Guessing Game!\n")
  print("I'm thinking of a number between 1 and 100.\n")
  #Generate the random number
  random_number = random.randint(1, 100)
  turns = difficulty()
  guess = 0

  while guess != random_number:
    print(f'You have {turns} attempts left to guess the correct number.\n')
    guess = int(input("Guess a number please: "))
    turns = compare_values(guess, random_number, turns)
    if turns == 0:
      print("You've run out of guesses, you lose!!!")
      return
    elif guess != random_number:
      print("Guess again please!")

game()
