import input
import requirements_module
import generate_passoword
import result_token
import text_create
import database





if __name__ == "__main__":
    user = input.Inputclass(input.Inputclass.input_fname(),input.Inputclass.input_lname(),input.Inputclass.input_birthday())

    token = True
    text_create.File_writer.open_file(user.fname)
    while token ==True:
#---------------------------------------------GET THE PASSWORD AND STORE IT AS password-------------------------------------------------------
        password = generate_passoword.Generate_pass.generate()
        if password == None:
            password = input.Inputclass.input_password()


        input.Inputclass.set_password(user,password)

#-----------------------------------ADD the CHeCKS ON PASSWORD -------------------------------------------------------------------------------
        #print("check len")
        length_token = requirements_module.RequirementsClass.check_length_of_password(user)
        #print("check fname")
        fname_token = requirements_module.RequirementsClass.check_first_name_in_password(user)
        #print("check lname")
        lname_token = requirements_module.RequirementsClass.check_last_name_in_password(user)
        #print("check birthday")
        birthday_token = requirements_module.RequirementsClass.check_date_of_birth_in_password(user)

        #print("chack numbers")
        number_token = requirements_module.RequirementsClass.check_numbers_in_password(user)
        #print("Check symbols")
        symbol_token = requirements_module.RequirementsClass.check_symbols_in_password(user)
        #print("check letters")
        letter_token = requirements_module.RequirementsClass.check_characters_in_password(user)
#------------------------------------------------Print out the results------------------------------------------------------------------------
        checks = []
        checks.append(result_token.Token_results.length_check(length_token))
        checks.append(result_token.Token_results.fname_check(fname_token,user.fname))
        checks.append(result_token.Token_results.lname_check(lname_token,user.lname))
        checks.append(result_token.Token_results.birthday_check(birthday_token))
        checks.append(result_token.Token_results.number_check(number_token))
        checks.append(result_token.Token_results.symbol_check(symbol_token))
        checks.append(result_token.Token_results.letter_check(letter_token))
        checks.append(requirements_module.RequirementsClass.check_capitol_in_password(user.password))
        checks.append(database.check_password_in_db(user.password))




#-----------------------------------------SAVE TO A FILE__________________________________________________________________________
        text_create.File_writer.save_file(user.fname,user.password,checks)


#----------------------------------------EXITING OR NOT--------------------------------------------------------------
        token = result_token.Token_results.are_you_done()
#------------------------------------------OUT oF LOOP GOODBYE ---------------------------------------------------------------------------------
    print(f"Thank you for using the password checker {user.fname}")
