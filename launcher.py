import Flask_WebApp_Service
import sqlite3
import os
import lib.sql.sqllite_lib
import lib.logger as logger

def check_db():
    find_db_name='RavenCloud.db'
    if os.path.isfile(find_db_name):
        logger.logger_printer(level='info',msg='The Datebase was Found Successfully !')
    elif not os.path.isfile(find_db_name):
        logger.logger_printer(level='error',msg='Database Not Found ! Generate the Database...Please Wait')
        lib.sql.sqllite_lib.init_sqllite()
        logger.logger_printer(level='info',msg='The Datebase was Generated Successfully !')

def banner():
    f = open('banner.txt')
    print(f.read())

def init_ravencloud():
    banner()
    check_db()
    Flask_WebApp_Service.Flask_WebApp_Start()
    
init_ravencloud()

