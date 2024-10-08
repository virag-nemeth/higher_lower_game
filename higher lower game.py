import random
import game_data
data = game_data.data

import art

def random_option(data, memory):
    """Randomly choose Option A and B, ensuring they are not in memory."""
    option_A = random.choice(data)
    option_B = random.choice(data)

    # Ensure option_A and option_B are different and not in memory
    while option_A == option_B or option_B in memory or option_A in memory:
        option_B = random.choice(data)

    return option_A, option_B

def compare_followers(option_A, option_B):
    """Compare followers and return the winner option and user choice."""
    follower_A = option_A['follower_count']
    follower_B = option_B['follower_count']

    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if follower_A > follower_B:
        return "a", user_choice
    else:
        return "b", user_choice

def game_logic():
    """Main game loop."""
    print(art.logo)
    score = 0
    memory = []  # Memory list to store used options

    option_A, option_B = random_option(data, memory)  # Initial random options

    game_on = True

    while game_on:
        # Print comparison
        print(f"Compare A: {option_A['name']}, a {option_A['description']}, from {option_A['country']}")
        print(art.vs)
        print(f"Against B: {option_B['name']}, a {option_B['description']}, from {option_B['country']}")

        # Compare followers and get user input
        winner_option, user_choice = compare_followers(option_A, option_B)

        # Check if the user's guess is correct
        if user_choice == winner_option:
            score += 1
            print(f"You're right! Current score: {score}")

            # Add both options to memory
            memory.append(option_A)
            memory.append(option_B)

            # Re-randomise option_A and option_B
            option_A = option_B  # Previous option B becomes new option A
            option_B = random_option(data, memory)[1]  # Get a new option B

            # Clear the screen
            print("\n" * 20)
            print(art.logo)

        else:
            # User guessed wrong, game ends
            correct_answer = "A" if winner_option == "a" else "B"
            print(f"Sorry, that's wrong. The correct answer is {correct_answer}. Final score: {score}.")
            game_on = False


game_logic()
