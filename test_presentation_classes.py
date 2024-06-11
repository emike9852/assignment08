# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-test_presentation_classes.py
# # Description: Unit testing for presentation classes script
# ChangeLog: (Who, When, What)
# MEspinoza, 06/10/2024,Created Script
# ------------------------------------------------------------------------------------------------- #

import unittest
from unittest.mock import patch
from presentation_classes import IO

class testIO(unittest.TestCase):
    def setUp(self):
        self.employee_list = []

    def test_input_data_to_table(self):
        with patch('builtins.input', side_effect=('Mike', 'Espinoza','10')):
            IO.input_data_to_table(self.employee_list)
            self.assertEqual(len(self.employee_list,1))
            self.assertEqual(self.employee_list[0].first_name, "Mike")
            self.assertEqual(self.employee_list[0].last_name, "Espinoza")
            self.assertEqual(self.employee_list[0].empoyee_rating, 10)

    def test_input_data_to_table(self):
        with patch('builtins.input', side_effect=('Jane', 'Doe', 'invalid')):
            IO.input_data_to_table(self.employee_list)
            self.assertEqual(len(self.employee_list),0)

if __name__ == "__main__":
    unittest.main()