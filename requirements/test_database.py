import sqlite3

def create_db(conn, table_name):
    conn.execute(f'''CREATE TABLE {table_name}
                    (ID INTEGER PRIMARY KEY,
                    COMMONPASSWORDS TEXT)
                    ;''')
    print("Table created successfully")

def interate_pass(conn):
  file = open('passwords.txt','r')
  data = file.readlines()

  for common in data:
      print(common)
      command = f"INSERT INTO company (COMMONPASSWORDS) VALUES ('{common}');"
      conn.commit()
      conn.execute(command)
  return data

def get_values(conn):
    query = "SELECT * FROM company;"
    conn.commit()
    result = conn.execute(query).fetchall()
    print(result)

def main():
    conn = sqlite3.connect('test.db')
    print ("Opened database nicely")
    create_db(conn, 'company')
    # conn.close()
    results = interate_pass(conn)
    print('\nGetting values from DB:')
    get_values(conn)

    # command = f"INSERT INTO company (COMMONPASSWORDS) VALUES ('{results}');"
    # conn.commit()
    # conn.execute(command)
    # print("records created successfully")
    conn.close()

if __name__ == '__main__':
    main()
