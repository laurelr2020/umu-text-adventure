
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

    @staticmethod
    def management():
        print("Mangement: What is mangagement?\n" +
            "    A) the process of designing, launching and running a new business, which is often initially a small business.\n" +
            "    B) the business process of creating relationships with and satisfying customers. \n" +
            "    C) a set of principles relating to the functions of planning, organizing, directing and controlling,\n" +
            "      and the application of these principles in harnessing physical, financial, human and informational \n" +
            "      resources efficiently and effectively to achieve organizational goals.\n" + 
            "    D) the social science that studies the production, distribution, and consumption of goods and services\n"
        )

        correct_answer = "c"
        management_answer = input("Your answer > ")
        management_answer.replace(")", "")

        if(management_answer.lower() == correct_answer):
            business_degree = {'management' : "A+"}
        else:
            business_degree = {'management' : "F"}
        print("Grade: " + business_degree['management'])

    @staticmethod
    def marketing():
        print("Marketing: Which of the following is not inlcuded in marketing?\n" +
            "    A) Advertising products\n" +
            "    B) Selling products\n" +
            "    C) Delivering products\n"
            "    D) Firing employees"
        )