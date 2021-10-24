import unittest
from sexta_of_python.example_classes import Student


class TestStudent(unittest.TestCase):
    def setUp(self) -> None:
        self.student_1 = Student('JOHN', 'SILVA', 80, 'UFMG')
        self.student_2 = Student('maria', 'fernandes', 90, 'CEFET')
        self.student_3 = Student('Bruce', 'Lee', 82, 'PUC')
        self.student_4 = Student('Edgar', 'Poe', 88, 'virginia')
        print("Hi")

    def tearDown(self) -> None:
        print("Bye")
        
    def test_email(self):
        print("E-mail")
        # student_1 = Student('JOHN', 'SILVA', 80, 'UFMG')
        # student_2 = Student('maria', 'fernandes', 90, 'CEFET')
        # student_3 = Student('Bruce', 'Lee', 82, 'PUC')
        # student_4 = Student('Edgar', 'Poe', 88, 'virginia')

        # self.assertEqual(student_1.mail_address, 'john.silva@ufmg.com')
        # self.assertEqual(student_2.mail_address, 'maria.fernandes@cefet.com')
        # self.assertEqual(student_3.mail_address, 'bruce.lee@puc.com')
        # self.assertEqual(student_4.mail_address, 'edgar.poe@virginia.com')

        self.assertEqual(self.student_1.mail_address, 'john.silva@ufmg.com')
        self.assertEqual(self.student_2.mail_address, 'maria.fernandes@cefet.com')
        self.assertEqual(self.student_3.mail_address, 'bruce.lee@puc.com')
        self.assertEqual(self.student_4.mail_address, 'edgar.poe@virginia.com')

    def test_full_name(self):
        print("Full name")
        # student_1 = Student('JOHN', 'SILVA', 80, 'UFMG')
        # student_2 = Student('maria', 'fernandes', 90, 'CEFET')
        # student_3 = Student('Bruce', 'Lee', 82, 'PUC')
        # student_4 = Student('Edgar', 'Poe', 88, 'virginia')

        self.assertEqual(self.student_1.full_name, 'John Silva')
        self.assertEqual(self.student_2.full_name, 'Maria Fernandes')
        self.assertEqual(self.student_3.full_name, 'Bruce Lee')
        self.assertEqual(self.student_4.full_name, 'Edgar Poe')

    def test_study(self):
        print("Study")
        # student_1 = Student('JOHN', 'SILVA', 80, 'UFMG')
        # student_2 = Student('maria', 'fernandes', 90, 'CEFET')
        # student_3 = Student('Bruce', 'Lee', 82, 'PUC')
        # student_4 = Student('Edgar', 'Poe', 88, 'virginia')

        # self.student_1.study()
        # self.student_2.study()
        # self.student_3.study()
        # self.student_4.study()

        self.student_1.study()
        self.student_2.study()
        self.student_3.study()
        self.student_4.study()

        self.assertEqual(self.student_1.average_grade, 88)
        self.assertEqual(self.student_2.average_grade, 99)
        self.assertEqual(self.student_3.average_grade, 90.2)
        # self.assertEqual(student_3.average_grade, 90.1)
        self.assertEqual(self.student_4.average_grade, 96.8)
