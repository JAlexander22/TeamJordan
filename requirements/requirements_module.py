import json

# with open('json_storage/requirements.json', 'r') as file:
#     req = json.load(file)

class RequirementsClass:

    def __init__(self, first_name, last_name, date_of_birth, password):
        self.fname = first_name
        self.lname = last_name
        self.dob = date_of_birth
        self.password = password


    def check_length_of_password(self):
        length_check = True
        if len(self.password) < 8 or len(self.password) > 12:
            print("Total characters of password: ", len(self.password))
            print("Please create a password within the range of 8-12 characters")

            length_check = False
        return length_check


    def check_symbols_in_password(self):
        symbol_check = False
        symbols_in_password = False
        list_of_symbols = [
                            "`", "~", "!", "@", "#", "$", "%",
                            "^", "&", "*", "(", ")", "–", "_", "=", "+"]

        for symbol in list_of_symbols:
            if symbol in self.password:
                symbols_in_password = True
                symbol_check = True

        if symbols_in_password == False:
            print("You need to have at least one symbol in your password")

        return symbol_check


    def check_characters_in_password(self):
        charachter_check = False
        characters_in_password = False
        list_of_characters = [
                                "a", "b", "c", "d", "e", "f", "g", "h", "i",
                                "j", "k", "l", "m", "n", "o", "p", "q", "r",
                                 "s", "t", "u", "v", "w", "x", "y", "z"]

        for character in list_of_characters:
            if character in self.password.lower():
                characters_in_password = True
                charachter_check = True

        if characters_in_password == False:
            print("You need to have at least one letter in your password")

        return charachter_check


    def check_numbers_in_password(self):
        number_check = False
        numbers_in_password = False
        list_of_numbers = [
                            "0", "1", "2", "3", "4",
                             "5", "6", "7", "8", "9"]

        for number in list_of_numbers:
            if number in self.password:
                numbers_in_password = True
                number_check = True

        if numbers_in_password == False:
            print("You need to have at least one number in your password")

        return number_check


    def check_common_password(self):
        common_password_check = True
        common_password_list = [
            "123",
            "1234",
            "12345",
            "123456",
            "1234567",
            "12345678"]

        if any(self.password in s for s in common_password_list):
            print("This is a common password! Please type in a different password or generate one automatically")
            common_password_check = False

        return common_password_check


    def check_first_name_in_password(self):
        fname_check = True
        if self.fname in self.password:
            print("Can't include your name in your password! Please lease type in a different password or generate one automatically")
            fname_check = False

        return fname_check


    def check_last_name_in_password(self):
        lname_check = True
        if self.lname in self.password:
            print("Can't include your last name in your password! Please lease type in a different password or generate one automatically")
            last_name = False

        return lname_check


    def check_date_of_birth_in_password(self):
        birthday_check = True
        dob_in_password = False
        date_of_birth_array = ["01", "05", "1800"]
        for date in date_of_birth_array:
            if date in self.password:
                dob_in_password = True
                birthday_check = False

        if dob_in_password == True:
            print("Can't include your date of birth in your password! Please lease type in a different password or generate one automatically")

        return birthday_check


    # def check_date_of_birth_in_password(self):
    #     #date_of_birth_array = ["01", "05", "1800"]
    #     date_of_birth_array = self.date_of_birth
    #     full_date = date_of_birth_array[0]+date_of_birth_array[1]+date_of_birth_array[2]
    #     half_date = date_of_birth_array[1]+date_of_birth_array[2]
    #     year = date_of_birth_array[2]
    #     if full_date in self.password or half_date in self.password or year in self.password:
    #         print("Can't include your date of birth in your password! Please lease type in a different password or generate one automatically")


def main():
    print("------------ This is the requirements module ---------------")

    requirements_object = RequirementsClass("mo", "ali", "01/01/1800", "moali05~1800")
    #print("Total characters of password: ", len(requirements_object.password))
    requirements_object.check_length_of_password()
    requirements_object.check_symbols_in_password()
    requirements_object.check_characters_in_password()
    requirements_object.check_numbers_in_password()
    requirements_object.check_common_password()
    requirements_object.check_first_name_in_password()
    requirements_object.check_last_name_in_password()
    requirements_object.check_date_of_birth_in_password()

if __name__ == "__main__":
    main()
