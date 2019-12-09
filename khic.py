from questions import foreign_language_questions
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
    print('Welcome to KHIC')

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