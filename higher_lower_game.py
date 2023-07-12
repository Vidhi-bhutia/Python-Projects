import random
from higher_lower_game_data import data
from replit import clear
count = 0
while True:
    first = random.choice(data)
    second = random.choice(data)
    name1, name2 = first['name'], second['name']
    dis1, dis2 = first['description'], second['description']
    country1, country2 = first['country'], second['country']
    follower1, follower2 = first['follower_count'], second['follower_count']
    print("\n\n\n")
    print(f"Compare A: {name1}, a {dis1}, from {country1}")
    print("\n\n\n")
    print(f"Against B: {name2}, a {dis2}, from {country2}")
    
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    clear()
    if (user_choice == 'A'):
        if (follower1 > follower2):
            count += 1
            print(f"You're correct. Current score: {count}")
        else:
            print(f"Sorry that's wrong. Final score: {count}")
            break
    elif (user_choice == 'B'):
        if (follower2 > follower1):
            count += 1
            print(f"You're correct. Current score: {count}")
        else:
            print(f"Sorry that's wrong. Final score: {count}")
            break
    else:
        print("Wrong input!")
        break