import input
import requirements_module
import generate_passoword

if __name__ == "__main__":
    user = input.Inputclass(input.Inputclass.input_fname(),input.Inputclass.input_lname(),input.Inputclass.input_birthday())

    token = True

    while token ==True:
        password = generate_passoword.Generate_pass.generate()
