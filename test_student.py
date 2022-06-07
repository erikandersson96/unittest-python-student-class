import unittest
from student import Student 

class TestStudent(unittest.TestCase): 

    def setUp(self): # built in method in Unittest
        print('setUp')
        self.student = Student('John', 'Doe')


    def tearDown(self): # built in method in Unittest
        print('tearDown')


    def test_full_name(self): 
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'John Doe')


    def test_email(self): 
        print('test_email')
        self.assertTrue(self.student.email, 'john.doe@email.com')


    def test_alert_santa(self): 
        print('test_alert_santa')
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list) 


if __name__ == '__main__':
    unittest.main()
