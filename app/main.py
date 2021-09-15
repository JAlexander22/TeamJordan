import input
import requirements_module
import generate_passoword
import result_token

if __name__ == "__main__":
    user = input.Inputclass(input.Inputclass.input_fname(),input.Inputclass.input_lname(),input.Inputclass.input_birthday())

    token = True

    while token ==True:
#---------------------------------------------GET THE PASSWORD AND STORE IT AS password-------------------------------------------------------
        password = generate_passoword.Generate_pass.generate()
        if password == None:
            password = input.Inputclass.input_password()


        input.Inputclass.set_password(user,password)
#-----------------------------------ADD the CHeCKS ON PASSWORD -------------------------------------------------------------------------------
        print("check len")
        requirements_module.RequirementsClass.check_length_of_password(user)
        print("check fname")
        requirements_module.RequirementsClass.check_first_name_in_password(user)
        print("check lname")
        requirements_module.RequirementsClass.check_last_name_in_password(user)
        print("check birthday")
        requirements_module.RequirementsClass.check_date_of_birth_in_password(user)

#------------------------------------------------Print out the results------------------------------------------------------------------------
        result_token.Token_results.length_check(token)
        result_token.Token_results.fname_check(token)
        result_token.Token_results.lname_check(token)
        result_token.Token_results.birthday_check(token)
