import random
from os import system, name

from assets import HANGMANPICS, INTRO
from words import WORDS

LIFE = 7


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


if __name__ == "__main__":
    chosen_word = random.choice(list(WORDS)).upper()
    display = ["_" for i in range(len(chosen_word))]
    game_over = False
    damage = 0
    won = False
    guessed_letters = []
    clear()

    while 1:
        print(INTRO)
        print(" ".join(display) + "\n")
        if damage:
            print(HANGMANPICS[damage - 1])
        if game_over:
            break
        guess = input("Guess a letter: ").upper()
        if (len(guess) != 1) or (not guess.isalpha()):
            clear()
            print("Please enter a letter.")
            continue
        if guess in guessed_letters:
            clear()
            print("You already guessed that letter!")
            continue
        else:
            guessed_letters.append(guess)

        clear()
        guessed = False

        for pos, letter in enumerate(chosen_word):
            if letter == guess:
                display[pos] = letter
                guessed = True

        if guessed:
            print("You guessed a letter!")
        else:
            damage += 1
            print("That letter is not in the word!")

        if damage == LIFE:
            game_over = True

        if "_" not in display:
            game_over = True
            won = True

    if won:
        print("You won!")
        print(f"It took you {LIFE - damage} tries.\n")
        print(f"The word was {chosen_word}:")
        explanation = '\n\t'.join(WORDS[chosen_word])
        print(f"\t{explanation}\n")
    else:
        print("You lost!\n")
