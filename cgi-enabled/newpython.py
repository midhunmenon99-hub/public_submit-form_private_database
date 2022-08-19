#!/usr/bin/python3
import mysql.connector
import webbrowser

conn = mysql.connector.connect(user='root', password='SAVEearth16$',
                              host='10.0.1.168',database='cust_details')

if conn:
    print ("Connected Successfully")
else:
    print ("Connection Not Established")

select_employee = """SELECT * FROM employee"""
cursor = conn.cursor()
cursor.execute(select_employee)
result = cursor.fetchall()


p = []

tbl = print ("<tr><td>First Name</td><td>Last Name</td></tr>")
p.append(tbl)

for row in result:
    a = "<tr><td>%s</td>"%row[0]
    print ("p.append(a)")
    b = "<td>%s</td>"%row[1]
    print("p.append(b)")



if(conn.is_connected()):
    cursor.close()
    conn.close()
    print("MySQL connection is closed.") 
