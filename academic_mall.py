from ebb import enter_ebb_west, enter_ebb_south
from khic import enter_khic_north, enter_khic_east

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

def enter_academic_mall_from_ebb_south():
    print('You are in the Academic Mall. ' +
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
        enter_academic_mall_from_ebb_south()

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
    print('You are exiting the Academic Mall. Where would you like to go? Enter EBB, Exit Campus, or Enter Academic Mall')