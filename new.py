print("HTTP/1.0 200 OK\n")
import cgi
form = cgi.FieldStorage()
f_name=form["First_name"].value
s_name=form["Last_name"].value

print("<br><b>First Name</b>",f_name)
print("<br><b>Second Name</b>",s_name)
