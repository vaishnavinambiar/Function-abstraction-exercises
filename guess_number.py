import random

random_number = random.randrange(1, 10)

def main():
    print ""
    number = input("I have a number between 1 and 10. Can you guess my number? Please type your first guess: ")
    guess(number)

def guess(number1):
    correct = False
    while not correct:
        if number1 > random_number:
            print "Too high. Try again."
            print ""
        elif number1 < random_number:
            print "Too low. Try again."
            print ""
        elif number1 == random_number:
           break
        number1 = input ("What number do you guess? ")
    if number1 == random_number:
       playAagain = raw_input ("Excellent! You guessed the number! Would you like to play again (y or n)? ")
       if playAagain == "y":
            main()

main()
