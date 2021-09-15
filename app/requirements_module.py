import input

class RequirementsClass(input.Inputclass):

    def __init__(self):
        super().__init__()
        #self.fname = first_name
        #self.lname = last_name
        #self.dob = date_of_birth
        #self.password = password


    def check_length_of_password(self):


        if len(self.password) < 8  :
            print("Please create a password with at teast 8 characters")


    def check_common_password(self):
        common_password_list = [
            "123",
            "1234",
            "12345",
            "123456",
            "1234567",
            "12345678"]

        if any(self.password in s for s in common_password_list):
            print("This is a common password! Please type in a different password or generate one automatically")


    def check_first_name_in_password(self):
        if self.fname.lower() in self.password.lower():
            print("Can't include your name in your password! Please lease type in a different password or generate one automatically")


    def check_last_name_in_password(self):
        if self.lname.lower() in self.password.lower():
            print("Can't include your last name in your password! Please lease type in a different password or generate one automatically")


    def check_date_of_birth_in_password(self):
        #date_of_birth_array = ["01", "05", "1800"]
        date_of_birth_array = self.birthday
        full_date = date_of_birth_array[0]+date_of_birth_array[1]+date_of_birth_array[2]
        half_date = date_of_birth_array[1]+date_of_birth_array[2]
        year = date_of_birth_array[2]
        if full_date in self.password or half_date in self.password or year in self.password:
            print("Can't include your date of birth in your password! Please lease type in a different password or generate one automatically")
        #for date in date_of_birth_array:
        #
        #    if date in self.password:
        #        print("Can't include your date of birth in your password! Please lease type in a different password or generate one automatically")


def main():
    print("------------ This is the requirements module ---------------")

    requirements_object = RequirementsClass("mo", "ali", "01/01/1800", "moali05")
    #print("Total characters of password: ", len(requirements_object.password))
    requirements_object.check_length_of_password()
    requirements_object.check_common_password()
    requirements_object.check_first_name_in_password()
    requirements_object.check_last_name_in_password()
    requirements_object.check_date_of_birth_in_password()

if __name__ == "__main__":
    main()
