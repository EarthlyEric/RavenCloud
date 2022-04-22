import sqlite3

def init_sqllite():
    db = sqlite3.connect("RavenCloud.db")
    print("RavenCloud loacal DateBase Connected!")
    db.execute( "CREATE TABLE User_Data(uuid TEXT,username TEXT, password TEXT, email TEXT)")
   