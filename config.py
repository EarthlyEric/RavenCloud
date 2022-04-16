from configobj import ConfigObj

config = ConfigObj('./config.ini')

#Network
ip = config['Network']['ip']
port = int(config['Network']['port'])

#Development
flask_debug_text = config['Development']['flask_debug']
if flask_debug_text == 'True':
    flask_debug = True
elif flask_debug_text == 'Flase':
    flask_debug = False