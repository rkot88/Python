# importing random from external library

import random

print("---------------------------")
print("----------game-------------")
print("---------------------------")
print()

the_number = random.randint(0, 100)
guess = -1

name = input("Player whats your name ")

while guess != the_number:
    guess_text = input("Guess a number between 0 and 100: ")
    guess = int(guess_text)
    if guess > the_number:
        print("Sorry {1}, your number + {0} + is too high".format(guess, name))
        # .format method dzieki niej concate integera guess ze stringami jest mozliwy argument guess dostal wartosc {0} a argument name {1}
    elif guess < the_number:
        print("Sorry {}, your number  + {} + is too low".format(name, guess))
        #jezeli uloze argumenty w dobrej kolejnosci to nie musze numerowac w nawiasach {}
    else:
        print("WELL DONE! {}, wygrales kurwa zycie {} to ten numer!".format(name, guess))

