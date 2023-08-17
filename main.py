import random, os, sys

nums = [*range(1, 7)]

def main():
    user_input = input("\nPress 'ENTER' to roll the dice or type 'EXIT' to terminate the program:")
    if (user_input == "EXIT"):
        exit()
    else:
        dice1 = random.choice(nums)
        dice2 = random.choice(nums)
        print(str(dice1) + " : " + str(dice2))
        os.execl(sys.executable, sys.executable, *sys.argv)  # restarts the program (optional)

main()
