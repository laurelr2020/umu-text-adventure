class User():
    def __init__(self):
        self.all_grades = {}
        self.computer_riddles_completed = 0

    @property
    def name(self):
        '''Name of current player'''
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def purple_raider(self):
        '''Identifies as a member of the University of Mount Union'''
        return self._purple_raider

    @purple_raider.setter
    def purple_raider(self, attend_umu):
        self._purple_raider = bool('yes' in attend_umu.lower())

    @property
    def business_grades(self):
        '''Grades received on business questions in EBB'''
        return self._business_grades
    
    @business_grades.setter
    def business_grades(self, grades_dict):
        self._business_grades = grades_dict
        self.all_grades.update(self._business_grades)

    @property
    def engineering_grades(self):
        '''Grades received on engineering questions in EBB'''
        return self._engineering_grades

    @engineering_grades.setter
    def engineering_grades(self, grades_dict):
        self._engineering_grades = grades_dict
        self.all_grades.update(self._engineering_grades)

    @property
    def psychology_grades(self):
        '''Grades received on psychology questions in EBB'''
        return self._psychology_grades

    @psychology_grades.setter
    def psychology_grades(self, grades_dict):
        self._psychology_grades = grades_dict
        self.all_grades.update(self._psychology_grades)

    @property
    def foreign_language_grades(self):
        return self._foreign_language_grades

    @foreign_language_grades.setter
    def foreign_language_grades(self, grades_dict):
        self._foreign_language_grades = grades_dict
        self.all_grades.update(self._foreign_language_grades)

    @property
    def computer_science_grades(self):
        return self._computer_science_grades

    @computer_science_grades.setter
    def computer_science_grades(self, grades_dict):
        self._computer_science_grades = grades_dict
        self.all_grades.update(self._computer_science_grades)

    @property
    def math_grades(self):
        return self._math_grades
    
    @math_grades.setter
    def math_grades(self, grades_dict):
        self._math_grades = grades_dict
        self.all_grades.update(self._math_grades)

    def printAllGrades(self):
        print(self.all_grades)