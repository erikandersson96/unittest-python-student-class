import unittest
from student import Student 
from datetime import timedelta

class TestStudent(unittest.TestCase): 

    @classmethod # built in method in Unittest
    def setUpClass(cls):
        print("set up class")


    def setUp(self): # built in method in Unittest
        print('setUp')
        self.student = Student('John', 'Doe')


    @classmethod # built in method in Unittest
    def tearDownClass(cls):
        print("tear down Class")


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


    def test_apply_extension(self): 
        old_end_date = self.student.end_date
        self.student.apply_extension(5)

        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))


if __name__ == '__main__':
    unittest.main()
