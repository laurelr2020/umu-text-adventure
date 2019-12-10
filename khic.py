from questions import foreign_language_questions, computer_science_questions
def enter_khic_north():
    print('Welcome to KHIC! Would you like to go to the Foreign Language Department or the Circulation Desk?')
    choice = input('Language or Circulation').lower()

    if('lang' in choice):
        enter_foreign_language_dept()
    elif('circ' in choice):
        enter_circulation_desk()
    else:
        enter_khic_north()

def exit_khic_north():
    print('You have exited KHIC North')

def enter_khic_east():
    print('Welcome to KHIC. Would you like to go to the Computer Science Department or 24-hour area?')
    choice = input('CS dept or 24-Hour Area').lower()

    if('cs' in choice):
        enter_cs_dept()
    elif('24' in choice):
        enter_twenty_four_hour_area()
    else:
        enter_khic_east()

def exit_khic_east():
    print('You have exited KHIC East')

def enter_cs_dept():
    print('Welcome to the Computer Science Deaprtment')
    computer_science_questions()
    exit_cs_dept()

def exit_cs_dept():
    print('You are exiting the CS Department. Where would you like to go? 24-Hour Area or Exit KHIC?')
    choice = input('24-Hour Area or Exit').lower()

    if('24' in choice):
        enter_twenty_four_hour_area()
    elif('exit' in choice):
        exit_khic_east()

def enter_foreign_language_dept():
    print('Welcome to the Foreign Language Department')
    foreign_language_questions()
    exit_foreign_language_dept()

def exit_foreign_language_dept():
    print('You have exit the Foreign Language Department. Where would you like to go? Circulation Desk or Exit KHIC')
    choice = input('Circulation or Exit').lower()

    if('circ' in choice):
        enter_circulation_desk()
    elif('exit' in choice):
        exit_khic_north()

def enter_circulation_desk():
    print('Welcome to the Circulation Desk')

def enter_twenty_four_hour_area():
    print('Welcome to the 24-Hour Area')