# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-test_presentation_classes.py
# # Description: Unit testing for processing classes script
# ChangeLog: (Who, When, What)
# MEspinoza, 06/10/2024,Created Script
# ------------------------------------------------------------------------------------------------- #

import unittest
import tempfile
import json
import data_classes as data
from processing_classes import FileProcessor

class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        self.sample_employee = [
            data.Employee("Mike","Espinoza", 10)
        ]
    def tearDown(self):
        self.temp_file.close

    def test_write_data_to_file(self):
        FileProcessor.write_data_to_file(self.temp_file_name,self.sample_employee)

        with open(self.temp_file_name,"r") as file:
            file_data = json.load(file)

        self.assertEqual(len(file_data), len(self.sample_employee))

if __name__ == "__main__":
    unittest.main()