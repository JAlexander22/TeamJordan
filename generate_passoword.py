import random
import string

# get random password pf length 8 with letters, digits, and symbols
class Generate_pass:

    def generate(self):

        while True:
            try:
                user = str(input('Do you want to generate a random password? Yes/No: '))
                if user == 'Yes':
                    while True:
                        characters = string.ascii_letters + string.digits + string.punctuation
                        password = ''.join(random.choice(characters) for i in range(8))
                        print ("Generated password is:", password)
                        second_response = input('Do you want a different password? Yes/No ')
                        if second_response == 'Yes':
                            continue
                        else:
                            print('Your new password is ', password)
                            break
                    break
                elif user == 'No':
                    print("No pass generated")
                    break
                else:
                    print ("Yes or No")
            except:
                continue

Password_Gen = Generate_pass()
Password_Gen.generate()
