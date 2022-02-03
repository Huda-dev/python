import mysql.connector

cnx = mysql.connector.connect(
    user='root',
    password='Huda@1983',
    host='localhost',
    database='sql_hr')
cursor = cnx.cursor()
query = """SELECT first_name, last_name FROM employees"""
first_name = ""
last_name = ""
cursor.execute(query)
for (first_name, last_name) in cursor:
    print(first_name + "                      " + last_name)
cnx.close()
