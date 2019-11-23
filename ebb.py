import sys
from khic import enter_khic_north, enter_khic_east
from questions import business_questions, engineering_questions
from academic_mall import enter_academic_mall, exit_academic_mall

def enter_ebb_south():
    print('Welcome to EBB! \nChoose where you want to go:' )
    choice = input('Business Department or Upstairs > ')

    if('bus' in choice.lower()):
        enter_bus_dept()
    elif('up' in choice.lower()):
        ebb_second_floor_south()
    else:
        enter_ebb_south()

def exit_ebb_south():
    print('You have exited EBB. Where would you like to go: EBB or Academic Mall?')
    choice = input('EBB or Academic Mall > ').lower()

    if(choice == 'ebb'):
        enter_ebb_south()
    elif('acad' in choice):
        enter_academic_mall()
    else:
        exit_ebb_south()

def enter_ebb_west():
    print('You are now in EBB. Where you would like to go? Engineering Department, Upstairs, Exit EBB.')
    choice = input('Engineering, Upstairs, or Exit > ').lower()

    if('eng' in choice):
        enter_engineering_dept()
    elif('up' in choice):
        ebb_second_floor_north()
    elif('exit' in choice):
        exit_ebb_west()
    else:
        enter_ebb_west()


def exit_ebb_west():
    print('You have exited EBB. You are now in the Academic Mall.\n' +
    'Where would you like to go? EBB, KHIC North, KHIC West or South.')
    choice = input('EBB, North, West, or South > ').lower()

    if('ebb' in choice):
        enter_ebb_west()
    elif('north' in choice):
        enter_khic_north()
    elif('west' in choice):
        enter_khic_east()
    elif('south' in choice):
        exit_academic_mall()
    else:
        exit_ebb_west()

def ebb_second_floor_north():
    print('You are on the second floor\n' + 
    'Where would you like to go? EBB Lounge, Computer Lab, Down the Hallway, or Downstairs?')
    choice = input('Lounge, Lab, Hallway or Downstairs > ').lower()

    if('lounge' in choice):
        enter_ebb_lounge()
    elif('lab' in choice):
        enter_ebb_computer_lab()
    elif('hall' in choice):
        ebb_second_floor_south()
    elif('down' in choice):
        ebb_first_floor_south()
    else:
        ebb_second_floor_south()

def ebb_first_floor_south():
    print('You are in the lobby of EBB')

def ebb_second_floor_south():
    print('You are on the second floor')

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
        ebb_second_floor_south()
    else:
        exit_ebb_south()

def enter_engineering_dept():
    print('Welcome to the Engineering Department!\n' +
        'Answer the following questions to get your Engineering Degree:\n\n'
    )
    engineering_questions()
    exit_engineering_dept()

def exit_engineering_dept():
    print('You are exiting the Engineering Department\n')
    print('Where would you like to go? Business Department, Upstairs, or Exit EBB\n')
    choice = input('Business Department, Upstairs, or Exit EBB > ').lower()

    if('bus' in choice):
        enter_bus_dept()
    elif('up' in choice):
        ebb_second_floor_north()
    elif('exit' in choice):
        exit_ebb_west()
    else:
        exit_engineering_dept()

def enter_ebb_computer_lab():
    print('You are in the EBB Computer Lab')

def enter_ebb_lounge():
    print('You are in the EBB Lounge')