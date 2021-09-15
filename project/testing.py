import sqlite3

conn = sqlite3.connect('test.db')
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
    data = file.readlines()

    for common in data:
        print(common)
    return data

results = interate_pass()

command = f"INSERT INTO company (COMMONPASSWORDS) VALUES ({results});"
conn.commit()
print("records created successfully")
conn.close()
