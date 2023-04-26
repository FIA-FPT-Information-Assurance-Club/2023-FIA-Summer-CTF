#!/usr/bin/env python3
import random
from datetime import datetime
import time
import os
from Crypto.Util.number import bytes_to_long

MAX_NUM = 2**32 - 1

def get_odd(num):
    return (str(round((num/MAX_NUM)*100, 2)) + '%', str(round((1 - num/MAX_NUM)*100, 2)) + '%')

def gen_num():
    return random.randrange(MAX_NUM)

def checkresult(dealer_num, next_num):
    if next_num < dealer_num:
        return 'S'
    else:
        return 'B' 
    

current_time = time.time()
# Better seed mean better random? Or is there another way?
random.seed(bytes_to_long(os.urandom(8)))

print("""
 _  _ ___    _       __ ___       _     _         _  
|_ |_) |    /   /\  (_   |  |\ | / \   /  |  | | |_) 
|  |   |    \_ /--\ __) _|_ | \| \_/   \_ |_ |_| |_) 
                                                  
      """)
print("Welcome to FPT Casino Club")
print("Today is " + str(datetime.fromtimestamp(current_time)))
print("""Rule: Player bet on the value of the next numer is bigger or smaller than the dealer's number
Win: Gain two times the amount of bet
Lose: Lose the amount of bet
    """)

player_start_money = 2023
dealer_start_money = int('2023'* 23)
while(True):
    print()
    dealer_num = gen_num()
    print(f"Your money: {player_start_money}")
    print(f"Dealer's number: {dealer_num}")
    print(f"""
Win percentage:
Smaller: {get_odd(dealer_num)[0]}
Bigger: {get_odd(dealer_num)[1]}          
          """)
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
    bet = input("Bigger or Smaller? (B/S): ")
    next_num = gen_num()
    print(f'Result: {next_num}')
    if checkresult(dealer_num, next_num) == bet:
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
    