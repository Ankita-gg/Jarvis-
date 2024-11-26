import sqlite3

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAE(1000))"
cursor.execute(query)

query = "INSERT INTO sys_command VALUES (null,'Embarcadero Dev-C++', 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Embarcadero Dev-C++')"
cursor.execute(query)
con.commit()
