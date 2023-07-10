import pyfiglet
import csv
import random
from hangman_art import *

title = pyfiglet.figlet_format("Hangman", font='big')

num_of_incorrect = {0: none,
                    1: head,
                    2: body,
                    3: left,
                    4: right,
                    5: left_leg,
                    6: lose}
num = 0
print(title)
not_correct = True
alive = True

reader = csv.reader(open('words.csv', 'r'))
words = sum([word for word in reader], [])

word = random.choice(words)
word = word.strip()

blank = ["_" for letter in word]
already_guessed = []
while not_correct and alive:
    try:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or guess.isalpha() is False or guess in already_guessed:
            raise ValueError
    except ValueError:
        print("must be one new letter")
    else:
        already_guessed.append(guess)
        if guess not in word:
            num += 1
            print(num_of_incorrect[num])
            print(f"{guess} is not in the word.")
        elif guess in word:
            print(num_of_incorrect[num])
            print(f"{guess} is in the word!")
            for i in range(len(word)):
                if word[i] == guess:
                    blank[i] = guess

    print("".join(blank))
    if "_" not in blank:
        print('You win!')
        not_correct = False
    if num == 6:
        print(f"You lose, the word was {word}")
        alive = False
