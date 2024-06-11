import unittest
from data_classes import Person, Employee

class TestPerson(unittest.TestCase):

    def test_person_init(self):
        test_person = Person("Mike", "Espinoza")
        self.assertEqual(test_person.first_name,"Mike")
        self.assertEqual(test_person.last_name, "Espinoza")

    def test_person_invalid_name(self):
        with self.assertRaises(ValueError):
            Person("123","Doe")
        with self.assertRaises(ValueError):
            Person("John", "123")
    
    def test_person_str(self):
        person = Person("Mike", "Espinoza")
        string_representation = str(person)
        expected_value = "Mike,Espinoza"
        self.assertEqual(string_representation,expected_value)

class TestEmployee(unittest.TestCase):

    def test_employee_init(self):
        employee = Employee("Mike", "Espinoza", 10)
        self.assertEqual(employee.first_name, "Mike")
        self.assertEqual(employee.last_name, "Espinoza")
        self.assertEqual(employee.employee_rating, 10)

    def test_employee_rating_type(self):
        with self.assertRaises(ValueError):
            Employee("Mike", "Espinoza", "invalid_rating")
        
    def test_employee_str(self):
        employee = Employee("Mike", "Espinoza", 10)
        result = str(employee)
        expected_result = "Mike, Espinoza, 10"
        self.assertEqual(result, expected_result)

if __name__ =="__main__":
    unittest.main()