# Zgadywanie słowa
# Komputer wybiera losowo słowo
# Gracz wskazuje pięć liter
# Jeśli litery znajdują się w danym słowie, program informuje o tym
# Celem gracza jest odgadniecie słowa

import random

print('Program wybierze z puli jakieś słowo. Twoim zadaniem będzie odgadnąć jakie to słowo, po wprowadzeniu 5 wybranych liter.\n')

# Pula słów do wybrania przez program
WORDS = ('klepsydra', 'marynarz', 'kredyt', 'ambulans', 'eskimos')

# Wybór słowa przez program
word = random.choice(WORDS)
    
# Wprowadzenie liter użytkownika
letters = []
while len(letters) < 5:
    letter = input('Wprowadz literę: ')
    if len(letter) != 1:
        print('Zła wartośc, wprowadz jedną literę.\n')
        continue
    letters.append(letter)
    if letter in word:
        print('Ta litera ZNAJDUJE się w słowie! ;)\n')
    else: print('Ta litera NIE ZNAJDUJE się w słowie! ;(\n')

# Przedstawienie liter użytkownika i próba odgadnięcia hasła
print(f'Litery które wybrałeś to: ', end="")
for letter in letters:
    print(letter, end=' ')

print('\n\nSpróbuj odgadnąć hasło!')

def show_word():
    word_to_guess = '_ ' * len(word)
    for letter in letters:
        i = 0
        for j in word:
            if letter == j:
                word_to_guess = word_to_guess[:i] + letter + word_to_guess[i+1:]
            i += 2
    return word_to_guess

answer = None
while answer != word:
    print(show_word())
    answer = input()
    if answer == word:
        print('ZWYCIĘSTWO !!!')
    else: print("Spróbuj ponownie! \n")