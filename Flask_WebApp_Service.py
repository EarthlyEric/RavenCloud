from gevent import monkey; monkey.patch_all()
from flask import Flask,render_template,redirect,url_for,send_from_directory,request
from gevent.pywsgi import WSGIServer
from flask_compress import Compress
from threading import Thread
import os,lib.config as config

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
    print('Flask_WebApp Server Start!')
    http_server.serve_forever()

def Flask_WebApp_Start():  
    service = Thread(target=run)
    service.start()
    


    
