import sys
from questions import quiz_user

def enter_ebb_south():
    print("Welcome to EBB! \nChoose where you want to go:" )
    choice = input("Business Department or Upstairs > ")

    if("bus" in choice.lower()):
        enter_bus_dept()
    elif("up" in choice.lower()):
        ebb_second_floor()
    else:
        print("You didn't enter a valid option. Bye, Bye.")
        sys.exit()

def enter_bus_dept():
    print("Welcome to the Business Department!\n" +
        "Answer the following questions to get your business degree:\n\n")
    
    quiz_user();

def ebb_second_floor():
    print("You're on the second floor")

