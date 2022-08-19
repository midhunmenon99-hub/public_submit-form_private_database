#!/usr/bin/python3

import mysql.connector

try:
    connection = mysql.connector.connect(host='10.0.1.168',
                                         database='cust_details',
                                         user='root',
                                         password='SAVEearth16$')

    sql_select_Query = "select * from customer"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    for row in records:
        print("First name = ", row[0], )
        print("Last name = ", row[1], "\n")
        

except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MySQL connection is closed")
