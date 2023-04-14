#!/usr/bin/python3

import random
from datetime import datetime
import time

def roll_dice():
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    roll3 = random.randint(1,6)
    total = roll1 + roll2 + roll3
    print(f"Result: {roll1} + {roll2} + {roll3} = {total}")
    return total

def checkresult(total):
    if total >= 3 and total <= 10:
        return 'S'
    elif total >= 11 and total <= 18:
        return 'B'

current_time = time.time()
random.seed(round(current_time))
print(current_time)

print("""
 _  _ ___    _       __ ___       _     _         _  
|_ |_) |    /   /\  (_   |  |\ | / \   /  |  | | |_) 
|  |   |    \_ /--\ __) _|_ | \| \_/   \_ |_ |_| |_) 
                                                  
      """)
print("Welcome to FPT Casino Club")
print("Today is " + str(datetime.fromtimestamp(current_time)))
print("""Rule: Player bet on the total number of dot in 3 dice
- 3-10: Small
- 11-18: Big
Win: Gain two times the amount of bet
Lose: Lose the amount of bet
    """)

player_start_money = 2023
dealer_start_money = int('2023'* 23)
while(True):
    print(f"Your money: {player_start_money}")
    try:
        money = int(input("Enter bet: "))
    except KeyboardInterrupt:
        break
    except:
        print("Invalid bet")
        continue
    if money > player_start_money or money < 0:
        print("Invalid bet")
        continue
    bet = input("Big or Small? (B/S): ")
    total = roll_dice()

    if checkresult(total) == bet:
        print("You win")
        player_start_money += money
        dealer_start_money -= money
    else:
        print("You lose")
        player_start_money -= money
        dealer_start_money += money
    if player_start_money <= 0:
        print("Out of money")
        break
    if dealer_start_money <= 0:
        with open("flag.txt") as f:
            print(f.read())
        break