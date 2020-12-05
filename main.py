from db import ToythonDB

mydb = ToythonDB("./mydb.db")
mydb.set("name", "Eren")
print(mydb.get("name"))