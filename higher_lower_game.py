from higher_lower_game_data import data
from higher_lower_art import logo, vs
import random
from replit import clear
'''
This code creates the higher/lower game for a user to play.
'''

def format_data(account):
    """Acquire and Format the neccesarry account data"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f'{account_name}, a {account_description}, from {account_country}'


def compare_accounts(guess, first_followers_count, second_followers_count):
    """Ingest the user guess, grab the follower counts, and check if the user's guess is correct"""
    if first_followers_count > second_followers_count:
        return guess == "A"
    else:
        return guess == "B"


def main():
    """Main logic of the code"""
    print(logo)
    score = 0 #Initialize the score counter variable
    continue_game = True
    second_account = random.choice(data) #Initialize this variable outside the loop to allow for switching of accounts

    #TODO Make it Repeatable
    while continue_game == True:
        # TODO: Grab the two accounts to compare
        first_account = second_account
        second_account = random.choice(data)
        while first_account == second_account: #Make sure the accounts are different before comparing
            second_account = random.choice(data)

        print(f'Compare A: {format_data(first_account)}.')
        print(vs)
        print(f'Against B: {format_data(second_account)}.')

        # TODO: Ask the user to guess who has more followers
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        # TODO: Get the follower count and check if the guess was correct
        first_followers_count = first_account["follower_count"]
        second_followers_count = second_account["follower_count"]
        answer_result = compare_accounts(guess, first_followers_count, second_followers_count)

        clear()
        print(logo)

        # TODO: User feedback regarding the guess
        if answer_result:  # This value is boolean
            score += 1
            print(f"Correct! You currently have {score} points!\n")
        else:
            continue_game = False
            print(f"Nope! The final score is: {score} points.\n")


if __name__ == '__main__':
    main()
