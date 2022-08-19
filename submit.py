#!/usr/bin/python3

print("Content-Type:text/html")
print()
import cgi

print ("<h1>Welcome</h1>


form=cgi.FieldStorage()

First_name=form.getvalue("First_name")
Last_name=form.getvalue("Last_name")



import mysql.connector


con=mysql.connector.connect(
  host="localhost",
  user="root",
  password="mynewpassword",
  database="cust_details"
)

cur=con.cursor()

cur.execute("INSERT INTO customer VALUES (%s, %s)", (First_name,Last_name))
con.commit()
cur.close()
con.close()


print("<h3>record inserted.</h3>")