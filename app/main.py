import input
import requirements_module
import generate_passoword

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
        requirements_module.RequirementsClass.check_length_of_password(user)
