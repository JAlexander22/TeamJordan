def check_password_in_db(conn, table_name, password):
    password_in_db = False
    if conn.execute(f"SELECT 1 FROM {table_name} WHERE COMMONPASSWORDS = '{password}\n'").fetchone():
        print("Found!")
        password_in_db = True
    else:
        print("Not Found!")
    return password_in_db
    
def main():
    print("checking if password created is in commoon password database:")
    check_password_in_db(conn, 'common_passwords', 'brady')      # pass in the variable you created for password instead of 'brady' 
