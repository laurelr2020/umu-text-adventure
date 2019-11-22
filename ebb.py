import sys
from questions import business_questions
from questions import engineering_questions
from academic_mall import enter_academic_mall

def enter_ebb_south():
    print('Welcome to EBB! \nChoose where you want to go:' )
    choice = input('Business Department or Upstairs > ')

    if('bus' in choice.lower()):
        enter_bus_dept()
    elif('up' in choice.lower()):
        ebb_second_floor()
    else:
        print('You did not enter a valid option. Bye, Bye.')
        sys.exit()

def exit_ebb_south():
    print('You have exited EBB. Where would you like to go: EBB or Academic Mall?')
    choice = input('EBB or Academic Mall > ').lower()

    if(choice == 'ebb'):
        enter_ebb_south()
    elif('acad' in choice):
        enter_academic_mall()
    else:
        sys.exit()

def enter_bus_dept():
    print('Welcome to the Business Department!\n' +
        'Answer the following questions to get your business degree:\n\n')
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
        exit_ebb_south()

def enter_engineering_dept():
    print('Welcome to the Engineering Department!\n' +
        'Answer the following questions to get your Engineering Degree:\n\n'
    )
    engineering_questions()
    exit_engineering_dept()

def exit_engineering_dept():


def ebb_second_floor():
    print('You are on the second floor')