import sqlite3
con = sqlite3.connect("cadastro.db") 

cur = con.cursor()

cur.execute("CREATE TABLE usuario(name, email, phone)")