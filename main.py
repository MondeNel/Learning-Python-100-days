import random
from art import logo, vs
from game_data import data

# Function to get a random account from the data
def get_random_account():
    return random.choice(data)

# Function to format the account data for printing
def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"

# Function to check if the user's guess is correct
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'A'
    else:
        return guess == 'B'

# Main game function
def game():
    print(logo)  # Print the game logo
    score = 0
    game_should_continue = True

    # Get the first two random accounts
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b  # The second account becomes the first account for the next round
        account_b = get_random_account()  # Get a new second account

        # Ensure the two accounts are not the same
        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        # Ask the user for their guess
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        a_follower_count = account_a['follower_count']
        b_follower_count = account_b['follower_count']
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1  # Increase the score if the guess is correct
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False  # End the game if the guess is incorrect
            print(f"Sorry, that's wrong. Final score: {score}.")

# Run the game
game()
