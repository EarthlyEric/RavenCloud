from configobj import ConfigObj

config = ConfigObj('./config.ini')

#Web
web_ip = config['Web']['ip']
web_port = int(config['Web']['port'])

#FTP
ftp_ip = config['FTP']['ip']
ftp_port = int(config['FTP']['port'])
ftp_max_connections = int(config['FTP']['max_connections'])
fto_max_connections_per_ip = int(config['FTP']['max_connections_per_ip'])

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