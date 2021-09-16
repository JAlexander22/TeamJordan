import random
import string

# get random password pf length 8 with letters, digits, and symbols
class Generate_pass:

    def generate():

        while True:
            try:
                user = str(input('Do you want to generate a random password or input one? Generate/Input: '))

                if user == 'Generate':
                    while True:
                        
                        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_letters

                        password_start = ''.join(random.choice(characters) for i in range(8))

                        password1 = ''.join(random.choice(string.digits) for i in range(1))
                        password2 = ''.join(random.choice(string.punctuation)for i in range(1))
                        password3 = ''.join(random.choice(string.ascii_letters) for i in range(1))
                        password4 = ''.join(random.choice(string.ascii_letters) for i in range(1))
                        password = password_start + password1 + password2 +password3.lower() +password4.upper()

                        print ("Generated password is:", password)
                        second_response = input('Do you want a different password? Yes/No ')
                        if second_response == 'Yes':
                            continue
                        else:
                            print('Your new password is ', password)
                            return password


                    break

                elif user == 'Input':
                    break
                else:
                    print ("Input or Generate")
            except:
                continue

if __name__ == "__main__":
    Password_Gen = Generate_pass()
    Password_Gen.generate()
