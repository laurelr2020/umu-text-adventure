import sys
from user import User
from ebb import enter_ebb_south
from academic_mall import enter_academic_mall

def enter_campus():
    print("You are coming into the Academic Mall on campus. Choose where you want to go:" )
    choice = input("EBB or North > ")
    
    if(choice.lower() == "ebb"):
        enter_ebb_south()
    elif(choice.lower() == "north"):
        enter_academic_mall()
    else:
        print("You didn't enter a valid option. Bye, Bye.")
        sys.exit()

def campus_intro():
    print("\nWell, that's not a problem. Let me tell you about this place." +
            " We use a lot of acronyms here at Mount Union so let me break it down for you.")
    print("EBB --> This is the Enginnering and Business Building. It houses the Engineering Department and the Business Department (creative, eh?).\n")
    print("T&H --> This building houses some brand new engineering labs on the first floor and the Psychology department on the second floor.\n")
    print("KHIC --> This building is lots of thing and it can get confusing so be careful not to get lost. " + 
            "This building houses some classrooms for all kinds of different classes. " +
            "It also houses the Foreign Languages Department, the Math Department, the Computer Science Department. " + 
            "Inside of it you will find the library along with lots of neat places to study. ")

def is_purple_raider():
    purple_raider = input("Do you attend the University of Mount Union? > ")

    if(purple_raider == 'yes'):
        knows_campus = input("Great!! Then you are familiar with the campus, yes? > ")
        if(knows_campus == 'yes'):
            print("Fantastic!! Let's get started!!")
        else:
            campus_intro()
    else:
        campus_intro()

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


def main():
    player = User()

    player.name = input("What's your name? > ")
    print(f"Hello {player.name}, Let's begin our adventure")

    rules()
    is_purple_raider()
    enter_campus()

if __name__ == '__main__':
    main()