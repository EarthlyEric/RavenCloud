import email
from gevent import monkey; monkey.patch_all()
from flask import Flask,render_template,request,redirect,url_for
from gevent.pywsgi import WSGIServer
from flask_compress import Compress
from flask_login import LoginManager, UserMixin, login_user, current_user, login_required, logout_user 
from threading import Thread
import lib.config as config
import lib.logger as logger
from lib.User import User

users = {'admin@example.com': {'password': 'password'}}  

app = Flask(__name__,
            static_url_path='', 
            static_folder='assets',
            template_folder='assets')

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'YourKey'  

login_manager = LoginManager(app)  

compress = Compress()
compress.init_app(app)

@login_manager.user_loader  
def user_loader(email):  
    if email not in users:  
        return  
  
    user = User()  
    user.id = email 
    return user  
  

@app.route('/')
def index():
    logger.logger_printer(level='info',msg=f'Visitor IP:{request.remote_addr},Request Home Page.')
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        logger.logger_printer(level='info',msg=f'Visitor IP:{request.remote_addr},Request Login Page.')

        return render_template('login.html')
    
        
    email = request.form['email']  
    if request.form['password'] == users[email]['password']:  
        #  實作User類別  
        user = User()  
        #  設置id就是email  
        user.id = email 
        #  這邊，透過login_user來記錄user_id，如下了解程式碼的login_user說明。  
        login_user(user)  
        #  登入成功，轉址  
        return redirect(url_for('dashboard'))  



    return 'Bad login'
    
@app.route('/dashboard')  
@login_required  
def dashboard():     
    if current_user.is_active:  
        return 'Logged in as: ' + current_user.id + 'Login is_active:True'
 
  
@app.route('/logout')  
def logout():  
    logout_user()  
    return 'Logged out'    

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


def run():
    http_server = WSGIServer((config.ip, config.port), app, log = None)
    logger.logger_printer(level='info',msg='WebApp Service Started !')
    http_server.serve_forever()

def Flask_WebApp_Start():  
    service = Thread(target=run)
    service.start()
    


    
