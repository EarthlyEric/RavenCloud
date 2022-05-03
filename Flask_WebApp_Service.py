from gevent import monkey; monkey.patch_all()
from flask import Flask,render_template,request
from gevent.pywsgi import WSGIServer
from flask_compress import Compress
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from threading import Thread
import lib.config as config
import lib.logger as logger


app = Flask(__name__,
            static_url_path='', 
            static_folder='assets',
            template_folder='assets')

app.config["TEMPLATES_AUTO_RELOAD"] = True

compress = Compress()
compress.init_app(app)

@app.route('/')
def index():
    logger.logger(level='info',msg=f'Visitor IP:{request.remote_addr},Request Home Page.')
    return render_template('index.html')

@app.route('/login')
def login():
    logger.logger(level='info',msg=f'Visitor IP:{request.remote_addr},Request Login Page.')
    return render_template('login.html')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


def run():
    http_server = WSGIServer((config.ip, config.port), app, log = None)
    logger.logger(level='info',msg='WebApp Service Started !')
    http_server.serve_forever()

def Flask_WebApp_Start():  
    service = Thread(target=run)
    service.start()
    


    
