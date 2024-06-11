from processing_classes import FileProcessor
from main import FILE_NAME
from main import employees

class IO:
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        print(message, end="\n\n")
        if error is not None:
            print("--Technical Error Message---")
            print(error, error.__doc__, type(error), sep='\n')
    
    @staticmethod
    def output_current_data(employee_data: list):
        print('='*40)
        for item in employee_data:
            print(f"FirstName: {item['FirstName']}, LastName: {item['LastName']}, EmployeeRating: {item['EmployeeRating']}")
        print('='*40, end='\n\n')
    
    @staticmethod
    def output_menu(menu:str):
        print(menu,end='\n\n')
    
    @staticmethod
    def input_menu_choice():
        choice = "0"
        try:
            choice = input("Enter the menu choice number: ")
            if choice not in ("1", "2", "3", "4"):
                raise Exception("You must choose 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return choice
    
    @staticmethod
    def input_data_to_table(employee_data: list):
        try:
            employee_first_name = input("Enter the employee's first name: ")
            if not employee_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            employee_last_name = input("Enter the employee's last name: ")
            if not employee_last_name.isalpha():
                raise ValueError("The employee's last name should not contain numbers.")
            employee_rating = input("Enter the rating for the employee: ")
            if not employee_last_name.isalpha():
                raise ValueError("The employee's last name should not contain nubmers")
            employee_data.append({"FirstName": employee_first_name, "LastName": employee_last_name, "EmployeeRating": employee_rating})
        except ValueError as e:
            IO.output_error_messages("Only use names without numbers", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error when adding data!", e)
        return employee_data

employee_table = FileProcessor.read_data_from_file(file_name=FILE_NAME, employee_data=employees)