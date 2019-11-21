import sys
from questions import business_questions

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
    business_questions()    
    exit_bus_dept()

def exit_bus_dept():
    print('You are exiting the Business Department.\n')
    print('Where to next? Engineering Department, Upstairs or Exit EBB\n')
    choice = input('Engineering, Upstairs, or Exit > ').lower()
    
    if('eng' in choice):
        enter_engineering_dept()
    elif('up' in choice):
        ebb_second_floor()
    else:
        exit_ebb()

def enter_engineering_dept():
    print('Welcome to the Engineering Department!\n' +
        'Answer the following questions to get your Engineering Degree:\n\n'
    )

def ebb_second_floor():
    print("You're on the second floor")

