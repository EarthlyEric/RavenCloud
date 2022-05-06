from time import sleep
import Flask_WebApp_Service
import lib.service.FTP as FTP
import os
import lib.sql.sqllite_lib
import lib.logger as logger
from configobj import ConfigObj

def check_db():
    find_db_name='RavenCloud.db'
    if os.path.isfile(find_db_name):
        logger.logger_printer(level='info',msg='The Datebase was Found Successfully !')
    elif not os.path.isfile(find_db_name):
        logger.logger_printer(level='error',msg='Database Not Found ! Generate the Database...Please Wait')
        lib.sql.sqllite_lib.init_sqllite()
        logger.logger_printer(level='info',msg='The Datebase was Generated Successfully !')

def check_secret_key():
    config = ConfigObj('./config.ini')
    if config['Security']['secret_key'] == '':
        logger.logger_printer(level='error',msg='The Secret Key Not Found ! Generate the The Secret Key...Please Wait')
        config['Security']['secret_key'] = f'{os.urandom(24)}'
        config.write()
    elif not config['Security']['secret_key'] == '':
        logger.logger_printer(level='info',msg='The Secret Key was Found Successfully !')  

def banner():
    f = open('banner.txt')
    print(f.read())

def init_ravencloud():
    banner()
    check_db()
    check_secret_key()
    sleep(0.1)
    FTP.FTP_Server_Start()
    Flask_WebApp_Service.Flask_WebApp_Start()
    
init_ravencloud()

