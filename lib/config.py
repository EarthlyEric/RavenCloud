from configobj import ConfigObj
from hamcrest import none

config = ConfigObj('./config.ini')

#Network
ip = config['Network']['ip']
port = int(config['Network']['port'])

#Security
secret_key=config['Security']['secret_key']

#Development
flask_debug_text = config['Development']['flask_debug']
if flask_debug_text == 'True':
    flask_debug = True
elif flask_debug_text == 'Flase':
    flask_debug = False

print(secret_key)
if secret_key == '':
    print('d')
elif not secret_key  == '':
    print('ss')