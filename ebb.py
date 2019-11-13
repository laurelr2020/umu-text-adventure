import sys

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

def enter_ebb_south():
    print("Welcome to EBB")

def enter_academic_mall():
    print("This is the Academic Mall. " +
        "To the left, you will see EBB. " + 
        "To the right, you will see the old part of KHIC " +
        "and straight ahead you see the new part of KHIC.")
    
