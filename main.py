from gevent import monkey; monkey.patch_all()
from flask import Flask,render_template,redirect,url_for,send_from_directory,request
from gevent.pywsgi import WSGIServer
from flask_compress import Compress
import os,config


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


if __name__ == "__main__":
    http_server = WSGIServer((config.ip, config.port), app)
    print('Server Start!')
    http_server.serve_forever()
    
    


    
