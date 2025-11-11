"""
Created on Mon Nov 10 22:19:46 2025
rock_paper_scissor
@author: Sherjahongir
"""

# rock_paper_scissor
# tosh, qog'oz, qaychi o'yini.

import random

emojis = { 'r': 'tosh', 's': 'qaychi', 'p': 'varaq' }
choices = ('r', 'p', 's')

while True:
  user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
  if user_choice not in choices:
    print('Invalid choice!')
    continue
  computer_choice = random.choice(choices)

  print(f'You chose {emojis[user_choice]}')
  print(f'Computer choise chose {emojis[computer_choice]}')

  if user_choice == computer_choice:
    print('Tie!') # durrang, teng.
  elif (
    (user_choice == 'r' and computer_choice == 's') or \
    (user_choice == 's' and computer_choice == 'p') or \
    (user_choice == 'p' and computer_choice == 'r')):
    print('You win')
  else:
    print('You lose')


  should_continue = input('Continue? (y/n): ').lower()
  if should_continue == 'n':
      break
  print("Thanks for playing!")



