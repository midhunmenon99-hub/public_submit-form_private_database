#!/usr/bin/python3

print("Content-Type:text/html")
print()
import cgi

form=cgi.FieldStorage()

First_name=form.getvalue("First_name")
Last_name=form.getvalue("Last_name")



import mysql.connector


con=mysql.connector.connect(
  host="10.0.1.168",
  user="root",
  password="SAVEearth16$",
  database="cust_details"
)

cur=con.cursor()

cur.execute("INSERT INTO customer VALUES (%s, %s)", (First_name,Last_name))
con.commit()
cur.close()
con.close()

print ("<h1>1 row inserted into database</h1>")

link = 'https://www.w3schools.com/'
print ("click here to retrieve results> {}".format(link))

#print ("<p><a href="https://www.w3schools.com/">click here to retrieve results</a></p>")
#print ("<form  action="/cgi-enabled/newpython.py" method="GET"> </form>")
#	<br><input type="submit" value="retrieve results">")
