class RequirementsClass:

    def __init__(self, first_name, last_name, date_of_birth, password):
        self.fname = first_name
        self.lname = last_name
        self.dob = date_of_birth
        self.password = password

    def check_common_password(self):
        common_password_list = ["123", "1234", "12345", "123456", "1234567", "12345678"]

        if any(self.password in s for s in common_password_list):
            print("This is a common password! Please type in a different password or generate one automatically")


    def check_first_name_in_password(self):
        if self.fname in self.password:
            print("Can't include your name in your password! Please lease type in a different password or generate one automatically")


    def check_last_name_in_password(self):
        if self.lname in self.password:
            print("Can't include your last name in your password! Please lease type in a different password or generate one automatically")


    def check_date_of_birth_in_password(self):
        date_of_birth_array = ["01", "01", "1800"]

        for date in date_of_birth_array:
            if date in self.password:
                print("Can't include your date of birth in your password! Please lease type in a different password or generate one automatically")


def main():
    print("------------ This is the requirements module ---------------")

    requirements_object = RequirementsClass("mo", "ali", "01/01/1800", "12mo345ali1800")
    requirements_object.check_common_password()
    requirements_object.check_first_name_in_password()
    requirements_object.check_last_name_in_password()
    requirements_object.check_date_of_birth_in_password()

if __name__ == "__main__":
    main()
