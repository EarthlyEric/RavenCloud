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
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

def run():
    http_server = WSGIServer((config.ip, config.port), app)
    logger.logger(level='info',msg='WebApp Service Started !')
    http_server.serve_forever()

def Flask_WebApp_Start():  
    service = Thread(target=run)
    service.start()
    


    
