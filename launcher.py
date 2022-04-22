import Flask_WebApp_Service
import sqlite3
import os
import lib.sql.sqllite_lib

def check_db():
    find_db_name='RavenCloud.db'
    if os.path.isfile(find_db_name):
        print('have')
    elif not os.path.isfile(find_db_name):
        lib.sql.sqllite_lib.init_sqllite()


def init_ravencloud():
    check_db()
    Flask_WebApp_Service.Flask_WebApp_Start()
    
init_ravencloud()