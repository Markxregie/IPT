import sqlite3

# Connect to the database
connect = sqlite3.connect('company.db')


# SQL statement for inserting data
strSQL = "SELECT * FROM Names"

# Execute the SQL statement
cursor = connect.cursor()
cursor.execute(strSQL)

rows = cursor.fetchall()

for row in rows:
    print(row)
# Commit the transaction
connect.commit()


# Close the cursor and connection
cursor.close()
connect.close()
