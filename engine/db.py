import sqlite3

con =sqlite3.connect("jarvis.db") 
#to add table 
cursor = con.cursor()

#Creating table
query ="CREATE TABLE IF NOT EXISTS sys_command(id integer primary key,name VARCHAR(100),path VARCHAR(1000))"
cursor.execute(query)

#//////instrting table /to add in table we replace nameof matlab and path given below
#query = "INSERT INTO sys_command VALUES (null,'matlab','C:\\Program Files\\MATLAB\\R2024b\\bin\\matlab.exe')"
#cursor.execute(query)
#con.commit()

#query = "DELETE FROM sys_command WHERE id=1"
#cursor.execute(query)
#con.commit()

#////create  web_table
query ="CREATE TABLE IF NOT EXISTS web_command(id integer primary key,name VARCHAR(100),url VARCHAR(1000))"
cursor.execute(query)

#to drop table
#query="DROP TABLE IF EXISTS web_command"
#cursor.execute(query)

query = "INSERT INTO web_command VALUES (null,'chatgpt','https://chatgpt.com/')"
cursor.execute(query)
con.commit()
