"""
26-dars:So'z topish o'yini. davomi.
Created on Wed Oct  1 20:29:28 2025
@author: Sherjahongir.
"""

import random
from uzwords import words

def get_word():
    word = random.choice(words)
    while "-" in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def display(user_letters,word):
    display_letter=""
    for letter in word:
        if letter in user_letters.upper():
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter

def play():
    word = get_word()
    # So'zdagi harflar
    word_letters = set(word)
    # Foydalanuvchi kiritgan harflar
    user_letters = ''
    print(f"Men {len(word)} xonali harf o'yladim. Topa olasizmi?")
    # print(word)
    while len(word_letters)>0:
        print(display(user_letters,word))
        if len(user_letters)>0:
            print(f"Shu vaqtgacha kiritgan harflaringiz: {user_letters}")
            
        letter = input("Xarf kiriting: ").upper()
        if letter in user_letters:
            print("Bu xarfni avval kiritgansiz. Boshqa harf kiriting.")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} xarfi to'g'ri.")
        else:
            print("Bunday xarf yo'q.")
        user_letters += letter
    print(f"Tabriklayman! {word} harfini {len(user_letters)} ta urinishda topdingiz.")


# Bu set buyrug'i so'zni harflarga bo'lib chiqadi va jadvalida bir harf 
# ikki marta takrorlanmaydi.

# word
# Out[44]: 'ОЛИБСОТАРЛИК'
# set(word)
# Out[45]: {'А', 'Б', 'И', 'К', 'Л', 'О', 'Р', 'С', 'Т'}


# O'ynash uchun play() deb concolega yozamiz.
