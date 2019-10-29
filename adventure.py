import sys

def is_purple_raider():
    purple_raider = input("Do you attend the University of Mount Union? > ")

def rules():
    print("\nOkay, let's get the ground rules out of the way first.")
    print("If you get asked a 'yes' or 'no' question, answer with 'yes' or 'no'.")
    understands = input("Get it? > ")

    if(understands.lower() == 'yes'):
        print("Good! Let's get started!")
    elif(understands.lower() == 'no'):
        print("Okay, I'll go over this one more time.")
        print("If a question can be answered with 'yes' or 'no', you must answer by typing 'yes' or no'.")
        understands = input("Get it? > ")
        if(understands.lower() == 'yes'):
            print("Good! Let's get started!")
        else: 
            print("I dont think this game is going to work out for you. Bye, bye.")
            sys.exit()
    else:
        print("If you can't understand these simple rules, you wont be able to play the game.")
        sys.exit()

def get_player_name():
    return input("What's your name? > ")

def welcome():
    player_name = get_player_name()
    print(f"Hello {player_name}, Let's begin our adventure")

def main():
    welcome()
    rules()

if __name__ == '__main__':
    main()