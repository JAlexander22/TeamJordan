
class Inputclass:
#---------------------------------------------------------DEFINE OBJECT---------------------------------------------------------------
    def __init__(self,fname,lname,birthday):
        self.fname = fname
        self.lname = lname
        self.birthday = birthday
        self.password = None
#------------------------------------------------------------FUNCTIONS-----------------------------------------------------------------
    def input_fname():            #gets an first name from the user, checks if it is valid
        counter = True
        while counter == True:
            first_name = input("What is your first name?")
            counter = Inputclass.check_str(first_name)

        return first_name

    def check_str(inp_str):
        exit_loop = False

        for element in inp_str:
            if element.isdigit():
                print("Please do not input numbers")
                exit_loop = True
            elif element == ' ':
                print("Please do not input spaces in the name")
                exit_loop = True
        return exit_loop

    def check_pass(inp_pass):
        exit_loop = False
        for element in inp_pass:
            if element == ' ':
                print("Please do not input spaces in the password")
                exit_loop = True
        return exit_loop

    def input_lname():
        counter = True
        while counter == True:
            last_name = input("What is your last name?")
            counter = Inputclass.check_str(last_name)
        return last_name

    def input_birthday():
        correct = False
        while correct == False:

            try:
                d = int(input("What is the day you were born? (dd)"))
                if d <= 31 and d >= 1:
                    m = int(input("What month were you bought? (mm)"))
                    if m <=12 and m >=1:
                        year = int(input("What year were you born? (yyyy)"))
                        if len(str(year)) == 4:
                            correct = True
                        else:
                            print("Please enter a 4 character year. e.g 2000")
                    else:
                        print("Please input a month between 1-12")
                else:
                    print("please input an correct day between 1-31")

            except Exception as e:
                print(e)
                print("Please input numbers for your date of birth")

        return [str(d),str(m),str(year)]

    def input_password():
        counter = True
        while counter == True:
            new_password = input("Please input a new password: ")
            counter = Inputclass.check_pass(new_password)
        return new_password



    def get_password(self):
        return self.password

    def set_password(self,password):
        self.password = password

if __name__ == "__main__":
    test = Inputclass(Inputclass.input_fname(),Inputclass.input_lname(),Inputclass.input_birthday())
    print(test)

    print("should be no password: ",test.get_password())

    test.set_password("secret")

    print(test.get_password())

    print(Inputclass.input_password())
