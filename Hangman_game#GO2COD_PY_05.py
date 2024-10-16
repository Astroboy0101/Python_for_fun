#GO2COD_PY_05
# By Kena Fayera
import random
from collections import Counter

words = '''dog,cat,elephant,giraffe,lion,tiger,
zebra,bear,kangaroo,panda,dolphin,penguin,owl,frog,turtle,rabbit,horse,eagle,shark,monkey'''

words = words.split(",")
word = random.choice(words)

if __name__ == '__main__':
    print(f'Guess the word! HINT: Word is a name of Animal. It contains {len(word)} letters.')

    for i in word:
        print("_",end=" ")
    print()

    playing = True
    letter_guessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        while (chances != 0) and flag == 0:
            print()
            chances -= 1

            try:
                guess = str(input("Enter a letter to guess: ")).lower()
            except:
                print("Enter only a letter!")
                continue
            if not guess.isalpha():
                print("Enter only a LETTER")
                continue
            elif len(guess) > 1:
                print("Enter only a SINGLE letter")
                continue
            elif guess in letter_guessed:
                print("You have already guessed that letter")
                continue
            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letter_guessed += guess
            for char in word:
                if char in letter_guessed and (Counter(letter_guessed)) != Counter(word):
                    print(char, end=" ")
                    correct += 1
                elif (Counter(letter_guessed) == Counter(word)):
                    print("The word is: ", end=" ")
                    print(word)
                    flag = 1
                    print("Congratulations, You won!")
                    break
                else:
                    print('_', end=" ")
        if chances <= 0 and (Counter(letter_guessed) != Counter(word)):
            print()
            print("You lost! Try again..")
            print("The word was {}".format(word))
    except KeyboardInterrupt:
        print()
        print("Bye! Try again.")
        exit()

