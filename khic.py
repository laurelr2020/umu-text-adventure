def enter_khic_north():
    print('Welcome to KHIC! Would you like to go to the Foreign Language Department or the Circulation Desk?')
    choice = input('Language or Circulation').lower()

    if('lang' in choice):
        enter_foreign_language_dept()
    elif('circ' in choice):
        enter_circulation_desk()
    else:
        enter_khic_north()

def enter_khic_east():
    print('Welcome to KHIC')

def enter_foreign_language_dept():
    print('Welcome to the Foreign Language Department')

def enter_circulation_desk():
    print('Welcome to the Circulation Desk')