class Person:
    def __init__(self, first_name: str, last_name:str):
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def first_name(self):
        return self.__first_name.title()
    
    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha() or value =="":
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers")

    @property
    def last_name(self):
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value =="":
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers")  

class Employee(Person):
    def __init__(self, first_name:str, last_name: str, employee_rating: str):
        super().__init__(first_name=first_name, last_name=last_name)
        self.employee_rating = employee_rating

    @property
    def employee_rating(self):
        return self.__employee_rating
    
    @employee_rating.setter
    def employee_rating(self, value: str):
        try:
            self.__employee_rating = value
        except ValueError:
            raise ValueError("You have entered an invalid rating!")
        
    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.employee_rating}"