
class business_questions():
    business_degree = {}

    @staticmethod
    def finance():
        print("Finance: What is a stock?\n" + 
            "    A) a type of investment that represents an ownership share in a company \n" +
            "    B) a garment for the foot and lower part of the leg \n" +
            "    C) life-threatening condition that occurs when the body is not getting enough blood flow \n" +
            "    D) a small amount of food eaten between meals\n"
        )

        correct_answer = "a"
        finance_answer = input("Your answer > ")
        finance_answer.replace(")", "")

        if(finance_answer.lower() == correct_answer):
            business_degree = {'finance' : "A+"}
        else:
            business_degree = {'finance' : "F"}
        print("Grade: " + business_degree['finance'])