import random
def roll_dice():
    roll = random.randint(0, 6)
    print ("You rolled: %s" % (roll))
    main()
def main():
    raw_input("Press enter to roll the dice")
    roll_dice()

main()
