from pyftpdlib.handlers import FTPHandler
import lib.logger as logger

class RVC_FTPHandler(FTPHandler):
    def on_connect(self):
        pass

    def on_disconnect(self):
        pass

    def on_login(self, username):
        logger.logger_printer(level='info',msg=f'FTP User: {username} Login !')
        