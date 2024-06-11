# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-processing_classes.py
# # Description: Python script for processing classes to data file
# ChangeLog: (Who, When, What)
# MEspinoza, 06/10/2024,Created Script
# ------------------------------------------------------------------------------------------------- #

import json
from presentation_classes import IO

class FileProcessor:
    @staticmethod
    def read_data_from_file(file_name: str, employee_data: list):
        try:
            file = open(file_name,"r")
            employee_data = json.load(file)
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!",e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error when reading the data file!",e)
        finally: 
            if file.closed == False: 
                file.close()
        return employee_data
    
    @staticmethod
    def write_data_to_file(file_name: str, employee_data: list):
        try:
            file = open(file_name, "w")
            json.dump(employee_data, file)
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally: 
            if file.closed == False:
                file.close()