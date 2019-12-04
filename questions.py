from config import player

def business_questions():
    business_degree = {
        'finance': '',
        'management': '',
        'marketing': ''
    }
    print('Finance: What is a stock?\n' + 
        '    A) a type of investment that represents an ownership share in a company \n' +
        '    B) a garment for the foot and lower part of the leg \n' +
        '    C) life-threatening condition that occurs when the body is not getting enough blood flow \n' +
        '    D) a small amount of food eaten between meals\n'
    )

    fin_correct_answer = 'a'
    finance_answer = input('Your answer > ')
    finance_answer.replace(')', '')

    if(finance_answer.lower() == fin_correct_answer):
        business_degree['finance'] = 'A+'
    else:
        business_degree['finance'] = 'F'
    print('Grade: ' + business_degree['finance'])
    
    print('Mangement: What is mangagement?\n' +
        '    A) the process of designing, launching and running a new business, which is often initially a small business.\n' +
        '    B) the business process of creating relationships with and satisfying customers. \n' +
        '    C) a set of principles relating to the functions of planning, organizing, directing and controlling,\n' +
        '      and the application of these principles in harnessing physical, financial, human and informational \n' +
        '      resources efficiently and effectively to achieve organizational goals.\n' + 
        '    D) the social science that studies the production, distribution, and consumption of goods and services\n'
    )
    mgt_correct_answer = 'c'
    management_answer = input('Your answer > ')
    management_answer.replace(')', '')

    if(management_answer.lower() == mgt_correct_answer):
        business_degree['management'] = 'A+'
    else:
        business_degree['management'] = 'F'
    print('Grade: ' + business_degree['management'])

    print('Marketing: Which of the following is not inlcuded in marketing?\n' +
        '    A) Advertising products\n' +
        '    B) Selling products\n' +
        '    C) Delivering products\n'
        '    D) Firing employees'
    )
    mkt_correct_answer = 'd'
    marketing_answer = input('Your answer > ')
    marketing_answer.replace(')', '')

    if(marketing_answer.lower() == mkt_correct_answer):
        business_degree['marketing'] = 'A+'
    else:
        business_degree['marketing'] = 'F'
    print('Grade: ' + business_degree['marketing'])
    
    player.business_grades = business_degree

# @staticmethod
# def graduation():
#     print('Let's look at how you did.')
#     for course, grade in business_degree.items():
#         print(f'course: {course} grade: {grade}\n')

#     earned_degree = all(value == 'A+' for value in business_degree.values())

#     if(earned_degree):
#         print('CONGRATULATIONS!!! You have earned business degree!!!!')
#     else:
#         print('I am sorry, but we are unable to award you a degree in business. Please feel free to take the courses again.')


def engineering_questions():
    engineering_grades = {
        'civil': '',
        'computer': '',
        'mechanical': '',
    }
    print('Civil Engineering: What is civil engineering?\n' +
    '    A) the process and the product of planning, designing, and constructing buildings or any other structures\n' + 
    '    B) a professional engineering discipline that deals with the design, construction, and maintenance of the physical and naturally built environment\n' +
    '    C) the use of computers to store, retrieve, transmit, and manipulate data, or information\n' +
    '    D) personal guarantees and freedoms that the government cannot abridge, either by law or by judicial interpretation, without due process\n'
    )

    civil_correct_answer = 'b'
    civil_answer = input('Your answer > ').replace(')', '')

    if(civil_answer.lower() == civil_correct_answer):
        engineering_grades['civil'] = 'A+'
    else:
        engineering_grades['civil'] = 'F'

    print('Grade: ' + engineering_grades['civil'])

    print('Computer Engineering: what is computer engineering?\n' +
        '    A)  the knowledge and ability to utilize computers and related technology efficiently\n' +
        '    B)  a machine that can be instructed to carry out sequences of arithmetic or logical operations automatically via computer programming.\n' +
        '    C)  a branch of engineering that integrates several fields of computer science and electronic engineering required to develop computer hardware and software\n' +
        '    D)  a branch of digital forensic science pertaining to evidence found in computers and digital storage media\n'
    )
    computer_correct_answer = 'c'
    computer_answer = input('Your answer > ').replace(')', '')

    if(computer_answer.lower() == computer_correct_answer):
        engineering_grades['computer'] = 'A+'
    else:
        engineering_grades['computer'] = 'F'

    print('Grade: ' + engineering_grades['computer'])

    print('Mechanical Engineering: what is mechanical engineering?\n' +
        '    A)  a measure of the force amplification achieved by using a tool,\n' +
        '    B)  the sum of potential energy and kinetic energy.\n' +
        '    C)  the discipline that applies engineering physics, engineering mathematics, and materials science principles to design, analyze, manufacture, \n' + 
        '    and maintain mechanical systems\n' +
        '    D)  an artisan, skilled tradesperson, or technician who uses tools to build, maintain, or repair machinery\n'
    )

    mechanical_correct_answer = 'c'
    mechanical_answer = input('Your answer > ').replace(')', '')

    if(mechanical_answer.lower() == mechanical_correct_answer):
        engineering_grades['mechanical'] = 'A+'
    else:
        engineering_grades['mechanical'] = 'F'

    print('Grade: ' + engineering_grades['mechanical'])

    player.engineering_grades = engineering_grades

def psychology_questions():
    psych_grades = {
        'cognitive' : '',
        'behavioral': '',
        'forensic' : ''
    }

    print('Cognitive Psychology: What is cognitive psychology?\n' + 
        '    A) an approach to psychology that emphasizes internal mental processes\n' +
        '    B) the branch of psychology concerned with the treatment of abnormal mentation and behavior\n' +
        '    C) the branch of psychology that studies the social and mental development of children\n' + 
        '    D) the psychological result of perception and reasoning'
    )
    
    cognitive_correct_answer = 'A'
    cognitive_answer = input('Your answer > ').replace(')', '')

    if(cognitive_answer.lower() == cognitive_correct_answer):
        psych_grades['cognitive'] = 'A+'
    else:
        psych_grades['cognitive'] = 'F'

    print('Behavioral Psychology: What is behaviourism\n' + 
        '    A) the aggregate of the responses made by an organism\n' +
        '    B) the interrelation of conscious and unconscious processes and emotions that determine personality and motivation\n' +
        '    C) the branch of social psychology that studies the psychodynamics of interaction in social groups\n' +
        '    D) an approach to psychology that emphasizes observable measurable behavior'
    )

    behavioral_correct_answer = 'D'
    behavioral_answer = input('Your answer > ').replace(')', '')
    
    if(behavioral_answer.lower() == behavioral_correct_answer):
        psych_grades['behavioral'] = 'A+'
    else:
        psych_grades['behavioral'] = 'F'

    print('Forensic Psychology: What is forensic psychology\n' + 
        '    A) the branch of psychology concerned with abnormal behavior\n' +
        '    B) the intersection between the study of psychology and the justice system\n' +
        '    C) the branch of psychology that is concerned with the physiological bases of psychological processes\n' +
        '    D) the branch of psychology that studies persons and their relationships with others and with groups and with society as a whole'
    )

    forensic_correct_answer = 'B'
    forensic_answer = input('Your answer > ').replace(')', '')
    
    if(forensic_answer.lower() == forensic_correct_answer):
        psych_grades['forensic'] = 'A+'
    else:
        psych_grades['forensic'] = 'F'

    player.psych_grades = psych_grades
