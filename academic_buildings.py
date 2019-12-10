import sys, time
from config import player
from riddles import ebb_computer_lab_riddles, get_riddle, tell_riddle
from questions import business_questions, engineering_questions, psychology_questions, foreign_language_questions, computer_science_questions, math_questions

def enter_campus():
    print('You are coming into the Academic Mall on campus. Where do you want to go: EBB or Continue North?' )
    choice = input('EBB or North > ')
    
    if(choice.lower() == 'ebb'):
        enter_ebb_south()
    elif(choice.lower() == 'north'):
        enter_academic_mall_north()
    else:
        enter_campus()

#
#Start Academic Mall
#
def enter_academic_mall_north():
    print('This is the Academic Mall. ' +
        'To the left, you will see EBB. ' + 
        'To the right, you will see the old part of KHIC ' +
        'and straight ahead you see the new part of KHIC.')
    print('Where would you like to go? EBB or Old KHIC or New KHIC?')
    choice = input('EBB or Old KHIC or New KHIC > ').lower()

    if('ebb' in choice):
        enter_ebb_west()
    elif('old' in choice):
        enter_khic_east()
    elif('new' in choice):
        enter_khic_north()
    else:
        enter_academic_mall_north()

def enter_academic_mall_south():
    print('You are in the Academic Mall. Where would you like to go? EBB or exit campus?')
    choice = input('EBB or Exit > ').lower()

    if('ebb' in choice):
        enter_ebb_south()
    elif('exit' in choice):
        exit_academic_mall()
    else:
        enter_academic_mall_south()

def exit_academic_mall():
    print('You are exiting the Academic Mall. Where would you like to go? Enter EBB or Exit Campus')
    choice = input('EBB or Exit').lower()

    if('ebb' in choice):
        enter_ebb_south()
    elif('exit' in choice):
        end_game()
    else:
        exit_academic_mall()
#
#End Academic Mall
#

#
#Start EBB
#
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
        enter_academic_mall_north()
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
        enter_academic_mall_south()
    else:
        exit_ebb_west()

def ebb_first_floor_north():
    print('You are now on the first floor of EBB. Where you would like to go? Engineering Department, Upstairs, Exit EBB.')
    choice = input('Engineering, Upstairs, or Exit > ').lower()

    if('eng' in choice):
        enter_engineering_dept()
    elif('up' in choice):
        ebb_second_floor_north()
    elif('exit' in choice):
        exit_ebb_west()
    else:
        enter_ebb_west()

def ebb_second_floor_north():
    print('You are on the second floor\n' + 
    'Where would you like to go? Down the Hallway or Downstairs?')
    choice = input('Hallway or Downstairs > ').lower()

    if('hall' in choice):
        ebb_second_floor_south()
    elif('down' in choice):
        ebb_first_floor_south()
    else:
        ebb_second_floor_south()

def ebb_first_floor_south():
    print('You are in the lobby of EBB\nChoose where you want to go:' )
    choice = input('Business Department or Upstairs > ')

    if('bus' in choice.lower()):
        enter_bus_dept()
    elif('up' in choice.lower()):
        ebb_second_floor_south()
    else:
        ebb_first_floor_south()

def ebb_second_floor_south():
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
        'Answer the following questions to get your Engineering Degree:\n\n')
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

def enter_psych_dept():
    print('You just entered the Psychology Department.\n\n' + 
        'Answer the following question to get your Psychology Degree\n\n')
    psychology_questions()
    exit_psychology_department()

def exit_psychology_department():
    print('You are exiting the Psychology Department.\n')
    print('Where would you like to go? Down the Hallway or Down the Stairs\n')
    choice = input('Hallway or Downstairs').lower()

    if('hall' in choice):
        ebb_second_floor_south()
    elif('down' in choice):
        ebb_first_floor_north()
    else:
        exit_psychology_department()

def enter_ebb_computer_lab():
    print('You are in the EBB Computer Lab.')
    choice = input('Wanna hear a riddle? > ').lower()

    if('yes' in choice):
        riddles = ebb_computer_lab_riddles()
        riddle = get_riddle(riddles, len(riddles))
        tell_riddle(riddles, riddle)
        riddles.remove(riddle)

        while(len(riddles) > 0):
            choice = input('Do you want to hear another one? > ')
            if('yes' in choice):
                riddle = get_riddle(riddles, len(riddles))
                tell_riddle(riddles, riddle)
                riddles.remove(riddle)
            else:
                break
        
        player.computer_riddles_completed = 0
        print('That is all the riddles for now. Continue with your adventure.')
        exit_ebb_computer_lab()
    else:
        ebb_second_floor_south()

def exit_ebb_computer_lab():
    print('You are in the hallway. Where would you like to go next? EBB Lounge, Downstairs, or Down the Hallway?')
    choice = input('Lounge, Downstairs, or Hallway > ')

    if('lounge' in choice):
        enter_ebb_lounge()
    elif('hall' in choice):
        ebb_second_floor_north()
    elif('down' in choice):
        ebb_first_floor_south()
    else:
        exit_ebb_computer_lab()

def enter_ebb_lounge():
    print('You are in the EBB Lounge.\n\n' + 
            'This is the EBB Lounge. To your right you will see a beautiful view of the campus quad.\n' + 
            'This is a fabulous study spot as there is comfortable seating and also some table to sit at to do study.\n')
    time.sleep(5)
    exit_ebb_lounge()

def exit_ebb_lounge():
    print('You are in the hallway. Where would you like to go next? EBB Computer Lab, Downstairs, or Down the Hallway?')
    choice = input('Lab, Downstairs, or Hallway > ')

    if('lab' in choice):
        enter_ebb_computer_lab()
    elif('hall' in choice):
        ebb_second_floor_north()
    elif('down' in choice):
        ebb_first_floor_south()
    else:
        exit_ebb_lounge()
#
#End EBB
#

#
#Start KHIC
#
def enter_khic_north():
    print('Welcome to KHIC! Would you like to go to the Foreign Language Department, the Circulation Desk, or Upstairs?')
    choice = input('Language, Circulation or Upstairs > ').lower()

    if('lang' in choice):
        enter_foreign_language_dept()
    elif('circ' in choice):
        enter_circulation_desk()
    elif('up' in choice):
        enter_khic_second_floor()
    else:
        enter_khic_north()

def exit_khic_north():
    print('You are in the Academic Mall. Where would you like to go: EBB, Old KHIC, or South')
    choice = ('EBB, KHIC, or South > ').lower()

    if('ebb' in choice):
        enter_ebb_west()
    elif('khic' in choice):
        enter_khic_east()
    elif('south' in choice):
        exit_academic_mall()
    else:
        exit_khic_north()

def enter_khic_east():
    print('Welcome to KHIC. Would you like to go to the Computer Science Department or 24-hour area?')
    choice = input('CS dept or 24-Hour Area > ').lower()

    if('cs' in choice):
        enter_cs_dept()
    elif('24' in choice):
        enter_twenty_four_hour_area()
    else:
        enter_khic_east()

def exit_khic_east():
    print('You have exited KHIC East. Where would you to go? EBB, New KHIC or Exit Academic Mall')
    choice = input('EBB, KHIC, or Exit > ').lower()

    if('ebb' in choice):
        enter_ebb_west()
    elif('khic' in choice):
        enter_khic_north()
    elif('exit' in choice):
        exit_academic_mall()
    else:
        exit_khic_east()

def enter_cs_dept():
    print('Welcome to the Computer Science Department')
    computer_science_questions()
    exit_cs_dept()

def exit_cs_dept():
    print('You are exiting the CS Department. Where would you like to go? 24-Hour Area or Exit KHIC?')
    choice = input('24-Hour Area or Exit > ').lower()

    if('24' in choice):
        enter_twenty_four_hour_area()
    elif('exit' in choice):
        exit_khic_east()
    else:
        exit_cs_dept()

def enter_foreign_language_dept():
    print('Welcome to the Foreign Language Department')
    foreign_language_questions()
    exit_foreign_language_dept()

def exit_foreign_language_dept():
    print('You have exited the Foreign Language Department. Where would you like to go? Circulation Desk, Upstairs or Exit KHIC?')
    choice = input('Circulation, Upstairs or Exit > ').lower()

    if('circ' in choice):
        enter_circulation_desk()
    elif('exit' in choice):
        exit_khic_north()
    elif('up' in choice):
        enter_khic_second_floor()
    else:
        exit_foreign_language_dept()

def enter_circulation_desk():
    print('Welcome to the Circulation Desk. \n' + 
        'Here you can checkout books with the student workers, or get help with research from a librarian.')
    time.sleep(3)
    exit_circulation_desk()

def exit_circulation_desk():
    print('Where would you like to go? 24-Hour Area or KHIC Lobby?')
    choice = input('24-Hour Area or Lobby > ').lower()

    if('24' in choice):
        enter_twenty_four_hour_area()
    elif('lobby' in choice):
        enter_khic_lobby_from_circ_desk()
    else:
        exit_circulation_desk()

def enter_khic_lobby_from_circ_desk():
    print('Where would you like to go? Foreign Language Department, Upstairs or Exit KHIC?')
    choice = input('Foreign Language, Upstairs or Exit > ').lower()

    if('fore' in choice):
        enter_foreign_language_dept
    elif('exit' in choice):
        exit_khic_north()
    elif('up' in choice):
        enter_khic_second_floor()
    else:
        enter_khic_lobby_from_circ_desk()

def enter_twenty_four_hour_area():
    print('Welcome to the 24-Hour Area.\n' +
    'In here you have the KHIC Cafe, you can get muffins there.\n'+
    'You also have the IT Helpdesk. They will help you with all your IT needs.' + 
    'Besides that, there are tables and study rooms that you can access 24/7.')
    time.sleep(3)
    exit_twenty_four_hour_area()

def exit_twenty_four_hour_area():
    print('You are exiting the 24-Hour area. Where would you like to go? Circulation Desk, CS Department, or Exit KHIC?')
    choice = input('Circulation, CS Dept or Exit > ').lower()

    if('circ' in choice):
        enter_circulation_desk()
    elif('cs' in choice):
        enter_cs_dept()
    elif('exit' in choice):
        exit_khic_east()
    else:
        exit_twenty_four_hour_area()

def enter_khic_second_floor():
    print('Welcome to the second floor of KHIC. Where would you like to go: Classrooms, Math Department, or Upstairs?')
    choice = input('Classrooms, Math Department, or Upstairs > ').lower()

    if('class' in choice):
        enter_classrooms()
    elif('math' in choice):
        enter_math_dept()
    elif('up' in choice):
        enter_khic_third_floor()
    else: 
        enter_khic_second_floor()

def exit_second_floor():
    print('You are on the first floor. Would you like to go to the Foreign Language Department, the Circulation Desk, or Upstairs?')
    choice = input('Language, Circulation or Upstairs > ').lower()

    if('lang' in choice):
        enter_foreign_language_dept()
    elif('circ' in choice):
        enter_circulation_desk()
    elif('up' in choice):
        enter_khic_second_floor()
    else:
        exit_second_floor()

def enter_classrooms():
    print('Here are three classrooms but,')
    time.sleep(1)
    print('shhhhhhhhhhhh\n\nclass is in session')
    time.sleep(2)
    exit_classrooms()

def exit_classrooms():
    print('Where would you like to go: Math Department, Upstairs, or Downstairs?')
    choice = input('Math Department, Upstairs, or Downstairs > ').lower()

    if('math' in choice):
        enter_math_dept()
    elif('up' in choice):
        enter_khic_third_floor()
    elif('down' in choice):
        exit_second_floor()
    else:
        exit_classrooms()

def enter_math_dept():
    print('Welcome to the Math Department. Answer the following questions to get your Math degree.')
    math_questions()
    exit_math_dept()

def exit_math_dept():
    print('You are exiting the Math Department. Where would you like to go: 2nd Floor Classrooms, Upstairs, or Downstairs?')
    choice = input('Classroom, Upstairs, or Downstairs > ').lower()

    if('class' in choice):
        enter_classrooms()
    elif('up' in choice):
        enter_khic_third_floor()
    elif('down' in choice):
        exit_second_floor()
    else:
        exit_math_dept()

def enter_khic_third_floor():
    print('Welcome to the third floor. It is quite a hike to get all the way up here but look at the view of campus.')
    time.sleep(2)

    print('There are study rooms, study booths, and study tables. Lots of studying goes on in these parts.')
    time.sleep(2)

    print('Also, there are some books you books that you can check out at the circulation desk.')
    time.sleep(2)

    print('We shall leave the studious students to their studies.')
    exit_third_floor()

def exit_third_floor():
    print('You are on the second floor of KHIC. Where would you like to go: Classrooms, Math Department, or Downstairs?')
    choice = input('Classrooms, Math Department or Downstairs > ').lower()

    if('class' in choice):
        enter_classrooms()
    elif('math' in choice):
        enter_math_dept()
    elif('down' in choice):
        exit_second_floor()
    else: 
        exit_third_floor()
#
#End KHIC
#

#----------
def end_game():
    print('Nice Job. Thanks for playing! Have a good day!')
    time.sleep(2)
    sys.exit()