import random, os, sys

nums = [*range(1, 7)]

def main():
    input("\nPress ENTER to roll the dice:\n")
    dice1 = random.choice(nums)
    dice2 = random.choice(nums)
    print(str(dice1) + " : " + str(dice2))
    os.execl(sys.executable, sys.executable, *sys.argv) #restarts the program (optional)


main()
