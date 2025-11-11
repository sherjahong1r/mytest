"""
Created on Mon Nov 10 22:17:50 2025
Son topish o'yini
@author: Sherjahongir
"""

print("\n\n")

# Son topish o'yini

import random


number_to_guess = random.randint(1, 100)
while True:
  try:
    guess = int(input('Guess the number between 1 and 100:' ))
    
    if guess < number_to_guess:
      print('Too low!')
    elif guess > number_to_guess:
      print('Too hight!')
    else:
      print('Congratulations! You guessed the number.')
  except ValueError:
    print('Please enter a valid number')
    
    
# Son topish o'yinining inglizcha varianti.
# 1 dan 100 gacha oraliqda kampiyuter bitta son o'ylaydi 
# va biz buni topishimiz kerak. 
    
    
    
    
    
    
    
    
    