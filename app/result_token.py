import json

with open('json_storage/requirements.json', 'r') as file:
    req = json.load(file)

class Token_results:



    def length_token(chk):
        if chk == True:
            print(f"The password FAILED the length check of between {req['min_length']} - {req['max_length']}")
        else:
            print("Your password has PASSED the length check")

    def fname_check(chk,name):
        if chk ==True:
            print(f"The password FAILED the first name check\n Please do not inlude {name}")
        else:
            print("Your password has PASSED the first name check")

    def lname_check(chk,name):
        if chk ==True:
            print(f"The password FAILED the last name check\n Please do not inlude {name}" )
        else:
            print("Your password has PASSED the last name check")

    def birthday_check(chk):
        if chk ==True:
            print(f"The password FAILED the birthday check\n Please do not inlude your birthday")
        else:
            print("Your password has PASSED the birthday check")


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
