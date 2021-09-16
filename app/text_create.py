
class File_writer:


    def open_file(name):
        try:
            with open(f"Password_storage/{name}.txt", "a") as file:
                file.close()
        except Exception as e:
            print(e)

    #def file_check(name):
    #    print(my_path.exists(f"Password_storage/{name}.txt"))

    def write_file(name,sentence):
        try:
            f = open(f"Password_storage/{name}.txt", "a")
            f.write(sentence)

            f.close()

        except Exception as e:
            print(e)

    def save_file(name,password,s_array):
        loop_token = True
        while loop_token == True:
            answ = input("Do you want to save to a file? Yes/No ")
            if answ == 'Yes':
                loop_token = False
                File_writer.write_file(name,f"The password checked was {password} \n")
                for item in s_array:
                    File_writer.write_file(name,item)
                    File_writer.write_file(name,"\n")
                File_writer.write_file(name,"\n ----------------------------------------------------------------------------------------------- \n")
            elif answ == 'No':
                loop_token = False
                return







if __name__ == "__main__":
    File_writer.open_file("jordan")
    File_writer.write_file("jordan","test")
    #File_writer.file_check("jordan","test")
    #my_path.exists(f"Password_storage/{name}.txt"
