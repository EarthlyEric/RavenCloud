import sqlite3

def init_sqllite():
    db = sqlite3.connect("RavenCloud.db")
    db.execute( "CREATE TABLE User_Data(user_id INTEGER PRIMARY KEY AUTOINCREMENT,email TEXT not null, password TEXT not null,username TEXT not null)")

def get_username_list():
    pass


   