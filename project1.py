#!/usr/bin/python

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mynewpassword",
  database="cust_details"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customer (First_name, Last_name) VALUES (%s, %s)"
val = ("John", "Doe")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
