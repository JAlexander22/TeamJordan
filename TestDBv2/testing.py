import sqlite3

# conn = sqlite3.connect('test.db')
# print ("Opened database nicely")
#
# conn.execute('''CREATE TABLE company
#                 (ID INT PRIMARY KEY,
#                 COMMONPASSWORDS TEXT)
#                 ;''')
# print("Table created successfully")
# conn.close()

def interate_pass():
    file = open('passwords.txt','r')


    for i in range(0, 5):
        conn = sqlite3.connect('test.db')
        data = file.readline()
        print(data)
        command = f"INSERT INTO company (COMMONPASSWORDS) VALUES ({data});"
        conn.execute(command)
        conn.commit()
        #eturn data

conn.close()
interate_pass()

#
# command = f"INSERT INTO company (COMMONPASSWORDS) VALUES ({results});"
# conn.commit()
# print("records created successfully")
