import sqlite3

# Create a SQL connection to our SQLite database
con = sqlite3.connect("MLDic.ml")

cur = con.cursor()

f=open("bo-bo.dic","a")
# The result of a "cursor.execute" can be iterated over by row
for row in cur.execute('SELECT word text,definition text FROM tbtb'):
    (bo,en) = row
    f.write(bo+" "+en+"\n")

# Be sure to close the connection
con.close()