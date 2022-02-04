############### Blackjack Project #####################
import random
from blackjack_art import logo

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over 21. You lose."
  if user_score == computer_score:
    return "Tie Game"
  elif computer_score == 0:
    return "You lose. The house has Blackjack"
  elif user_score == 0:
    return ("You win with a Blackjack!")
  elif user_score > 21:
    return ("You lose due to going over 21")
  elif computer_score > 21:
    return ("The house went over 21. You win!")
  elif user_score > computer_score:
    return ("You win!")
  else: 
    return ("The house wins. Better luck next time.")

def play_blackjack():
  print (logo)
  user_cards = [] #initialize the list of user cards
  computer_cards = [] #initialize the list of computer cards
  game_over = False #initialize the game over state for our while loop

  #Deal the first two cards to the player and the house
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  #User while loop
  while not game_over:
    user_score = calculate_score(user_cards)
    print(f'Your cards are: {user_cards}, their total value is: {user_score}')
    computer_score = calculate_score(computer_cards)
    print(f'The first house card is a: {computer_cards[0]} card.')

    if user_score == 0 or computer_score==0 or user_score > 21:
      game_over = True
    else:
        user_choice = input("Type 'yes' to be dealt another card or type 'pass' to pass: \n")
        if user_choice == "yes":
          user_cards.append(deal_card())
        else:
          game_over = True
  #Computer while loop for gameplay logic
  while computer_score != 0 and computer_score < 17:
      computer_cards.append(deal_card())
      computer_score = calculate_score(computer_cards)

  print(f'Your cards were: {user_cards}, the total value of those cards was: {user_score}')
  print("\n")
  print(f'The house cards were: {computer_cards}, the total value of those cards was: {computer_score}')
  print("\n")
  print (compare(user_score, computer_score))
  print("\n")

while input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ") == "yes":
  play_blackjack()

