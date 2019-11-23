import random 

def ebb_computer_lab_riddles():
    snack_riddle = {'How do computers snack?' : 'They eat cookies and spam one byte at a time'}
    alien_riddle = {"What is an alien's favorite place on a computer?" : 'The space bar'}
    glasses_riddle = {'Why did the computer get glasses?' : 'To improve his web sight'}
    tired_riddle = {'What does a computer do when it is tired?' : 'It crashes'}

    riddles = [snack_riddle, 
                    alien_riddle, 
                    glasses_riddle,
                    tired_riddle
    ]

    num = random.randrange(0, len(riddles), 1)
    return riddles[num]