import sqlite3
db = sqlite3.connect("RavenCloud.db")
db.execute("insert into User_Data values('admin','password','admin＠example.com')")