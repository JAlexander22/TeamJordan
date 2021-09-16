import json

with open('json_storage/requirements.json', 'r') as file:
    req = json.load(file)

class Token_results:



    def length_check(chk):
        if chk == False:
            print(f"The password FAILED the length check of between {req['min_length']} - {req['max_length']}")
            return f"The password FAILED the length check of between {req['min_length']} - {req['max_length']}"
        else:
            print("Your password has PASSED the length check")
            return "Your password has PASSED the length check"

    def fname_check(chk,name):
        if chk ==False:
            print(f"The password FAILED the first name check. Please do not include {name}")
            return f"The password FAILED the first name check. Please do not include {name}"
        else:
            print("Your password has PASSED the first name check")
            return "Your password has PASSED the first name check"

    def lname_check(chk,name):
        if chk ==False:
            print(f"The password FAILED the last name check. Please do not include {name}" )
            return f"The password FAILED the last name check. Please do not include {name}"
        else:
            print("Your password has PASSED the last name check")
            return "Your password has PASSED the last name check"

    def birthday_check(chk):
        if chk ==False:
            print("The password FAILED the birthday check. Please do not include your birthday")
            return "The password FAILED the birthday check. Please do not include your birthday"
        else:
            print("Your password has PASSED the birthday check")
            return "Your password has PASSED the birthday check"

    def number_check(chk):
        if chk ==False:
            print("The password FAILED the number check. Please include at least one number")
            return "The password FAILED the number check. Please include at least one number"
        else:
            print("Your password has PASSED the number check")
            return "Your password has PASSED the number check"

    def letter_check(chk):
        if chk ==False:
            print("The password FAILED the letter check. Please include at least one letter")
            return "The password FAILED the letter check. Please include at least one letter"
        else:
            print("Your password has PASSED the letter check")
            return "Your password has PASSED the letter check"

    def symbol_check(chk):
        if chk ==False:
            print("The password FAILED the symbol check. Please include at least one symbol")
            return "The password FAILED the symbol check. Please include at least one symbol"
        else:
            print("Your password has PASSED the symbol check")
            return "Your password has PASSED the symbol check"



    def are_you_done():
        out = True
        while out == True :
            ans = input("Are you finsihed? Yes/No ")
            if ans == 'Yes':
                return False

            elif ans =='No':
                return True


if __name__ == "__main__":
    token = True
    print(req)
    Token_results.length_token(token)
