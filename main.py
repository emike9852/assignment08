# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Main.py
# # Description: Main.py
# ChangeLog: (Who, When, What)
# MEspinoza, 06/10/2024,Created Script
# ------------------------------------------------------------------------------------------------- #

from presentation_classes import IO
from processing_classes import FileProcessor

# Defining constants
FILE_NAME: str = "EmployeeRatings.json"
MENU: str = """
----Employee Ratings ------------------------------
1. Show current employee rating data.
2. Enter new rating data.
3. Save data to a file.
4. Exit the program.
"""

# Defining variables
employees: list = []
menu_choice: str = ""

# Input from user
if __name__ == "__main__":
    while True:
        IO.output_menu(menu=MENU)
        menu_choice = IO.input_menu_choice()

    # Showing the current list of data
        if menu_choice == "1":
            IO.output_employee_data(employee_data=employees)
            continue
        
    # Entering an employee rating
        if menu_choice == "2":
            employee_table = IO.input_data_to_table(employee_data=employees)
            print("\n Here is the current list of data.")
            IO.output_employee_data(employee_data=employee_table)
            continue

    # Saving the data to a .json file
        if menu_choice =="3":
            FileProcessor.write_data_to_file(file_name=FILE_NAME, employee_data=employees)
            continue

    # Exiting the program
        elif menu_choice =="4":
            break