class Student:
    study_improve = 0.1

    def __init__(self, first_name: str, last_name: str, average_grade: int, institution: str):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.average_grade = average_grade
        self.institution = institution

    @property
    def mail_address(self):
        return f'{self.first_name.lower()}.{self.last_name.lower()}@{self.institution.lower()}.com'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def study(self):
        self.average_grade = round((1 + self.study_improve) * self.average_grade, 2)
