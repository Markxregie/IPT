import sqlite3

try:
    connect = sqlite3.connect('company.db')

    cursor = connect.cursor()
    print("The Database is Successfully Connected!")

    strSQl = "select Sqlite_version();"
    cursor.execute(strSQl)

    record = cursor.fetchall()
    print("SQlite Database Version is: ", record)

    cursor.close()

except sqlite3.Error as error:
    print("Error Qhile connecting to sqlite0", error)

finally:
    if connect:
        connect.close()
        print("The SQlite connection is closed")