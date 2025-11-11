"""
Created on Mon Nov 10 07:21:59 2025
dice_rolling_game.py
@author: Sherjahongir
"""

print("\n")

# Narda yani zar o'yini ishtirokchilarga son chiqaradi katta yoki kichik

import random

while True:
    choice = input('Roll the dice? (y/n): ').lower() # y=yes, n=no
    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1}, {die2})')
    elif choice == 'n':
        print('Thanks for playing!')
        break
    else:
        print('Invalid choice!')
        
        
        
        
        
# "Roll the dice?" ning tarjimasi:
# O‘zbekcha: "Kubikni ot(ing)?" yoki "Zarni tashlash?"
        
        
        
        
        
        
        
        
        
        
        
        