import random, time
from config import player

def ebb_computer_lab_riddles():
    snack_riddle = {'riddle' : 'How do computers snack?',
                    'answer' : 'They eat cookies and spam one byte at a time'
    }
    alien_riddle = {'riddle' : "What is an alien's favorite place on a computer?",
                    'answer' : 'The space bar'
    }
    glasses_riddle = {'riddle' : 'Why did the computer get glasses?',
                        'answer' : 'To improve his web sight'
    }
    tired_riddle = {'riddle' : 'What does a computer do when it is tired?',
                    'answer' : 'It crashes'}

    riddles = [snack_riddle, alien_riddle, glasses_riddle, tired_riddle]
    return riddles

def get_riddle(riddles, max_range):
    num = random.randrange(0, max_range, 1)
    return riddles[num]

def tell_riddle(riddles, riddle):
    print('\n' + riddle['riddle'])
    time.sleep(5)
    print(riddle['answer'] + '\n')
    player.computer_riddles_completed += 1
    return