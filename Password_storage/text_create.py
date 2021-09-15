
class File_writer:


    def open_file(name):
        try:
            with open(f"Password_storage/{name}.txt", "a+") as file:
                file.write(f"This is a storage of tested passwords for: {name} \n")
                file.close()
        except Exception as e:
            print(e)

    def file_check(name):
        print(my_path.exists(f"Password_storage/{name}.txt"))

    def write_file(name,sentence):
        try:
            f = open(f"Password_storage/jordan.txt", "a")
            f.write("test \n")

            f.close()

        except Exception as e:
            print(e)

if __name__ == "__main__":
    File_writer.open_file("jordan")
    File_writer.write_file("jordan","test")
    #File_writer.file_check("jordan","test")
    my_path.exists(f"Password_storage/{name}.txt"
