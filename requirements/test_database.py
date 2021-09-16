import sqlite3

def create_db(conn, table_name):
    conn.execute(f'''CREATE TABLE {table_name}
                    (ID INTEGER PRIMARY KEY,
                    COMMONPASSWORDS TEXT)
                    ;''')
    print("Table created successfully")

def interate_pass(conn, table_name):
  file = open('common_passwords.txt','r')
  data = file.readlines()

  for common in data:
      #print(common)         # Keep this commented, unless you want to see all 10,000 values printed individually on the terminal
      command = f"INSERT INTO {table_name} (COMMONPASSWORDS) VALUES ('{common}');"
      conn.commit()
      conn.execute(command)
  return data

def get_values(conn):
    query = "SELECT * FROM common_passwords;"
    conn.commit()
    result = conn.execute(query).fetchall()
    print(result)

def check_password_in_db(conn):

    if conn.execute("SELECT 1 FROM common_passwords WHERE COMMONPASSWORDS = '123456\n'").fetchone():
        print("Found!")
    else:
        print("Not Found!")

def main():
    conn = sqlite3.connect('common_passwords.db')
    print ("Opened database nicely")
    #create_db(conn, 'common_passwords')                       # 1. comment this after creatiing the database for the first time
    # conn.close()
    #results = interate_pass(conn, 'common_passwords')         # 2. comment this after creatiing the database for the first time
    #print('\nGetting values from DB:')                        # 3.1 uncomment this if you want to see the values from a table in the database
    #get_values(conn)                                          # 3.2 uncomment this if you want to see the values from a table in the database
    print("checking if password created is in commoon password database:")
    check_password_in_db(conn)
    conn.close()

if __name__ == '__main__':
    main()
