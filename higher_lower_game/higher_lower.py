from game_data import data
import random


choice_one = random.choice(data)

while True:
    choice_two = random.choice(data)
    print("\nWho has more followers?")
    print(f"Option A: {choice_one['name']}: {choice_one['description']} from {choice_one['country']}")
    print(f"Option B: {choice_two['name']}: {choice_two['description']} from {choice_two['country']}")

    player_choice = input("A / B: ").lower()
    print(f"\n{choice_one['name']} has {choice_one['follower_count']} followers")
    print(f"{choice_two['name']} has {choice_two['follower_count']} followers")

    
    if player_choice == "a" and choice_one['follower_count'] > choice_two['follower_count']:
        print("You win!")
    elif player_choice == "b" and choice_two['follower_count'] > choice_one['follower_count']:
        print("You win!")
        choice_one = choice_two
    else:
        print("You lose!")
        break
