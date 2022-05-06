import os
import logging
import lib.logger as logger
from pyftpdlib.log import config_logging
import lib.config as config
from pyftpdlib.authorizers import DummyAuthorizer 
from lib.service.FTP_Handler import RVC_FTPHandler
from pyftpdlib.servers import FTPServer
from threading import Thread




authorizer = DummyAuthorizer()
authorizer.add_user('user', '12345', './', perm='elradfmwMT')
handler = RVC_FTPHandler
handler.authorizer = authorizer
handler.banner = "Welcome to Use RavenCloud FTP Service !"
address = (config.ftp_ip, config.ftp_port)
server = FTPServer(address, handler)

server.max_cons = config.ftp_max_connections 
server.max_cons_per_ip = config.fto_max_connections_per_ip

config_logging(level=logging.ERROR)

def run():
    logger.logger_printer(level='info',msg='FTP Service Start !')
    server.serve_forever()

def FTP_Server_Start():
    service = Thread(target=run)
    service.start()