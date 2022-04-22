from datetime import datetime
from operator import le
from colored import fg, bg, attr


def nowtime():
    now = datetime.now()
    current_time = now.strftime('%Y/%m/%d %H:%M:%S')
    return current_time

def logger(level:str,msg:str):
    if level == 'info':
        print('[%s%s%s][%sINFO%s] %s%s %s' % (fg(153), nowtime(), attr(0) , fg(10), attr(0), fg(10), msg, attr(0)))
    elif level == 'warn':
        print('[%s%s%s][%sWarn%s] %s%s %s' % (fg(153), nowtime(), attr(0) , fg(184), attr(0), fg(184), msg, attr(0)))
    elif level == 'error':
        print('[%s%s%s][%sERROR%s] %s%s %s' % (fg(153), nowtime(), attr(0) , fg(196), attr(0), fg(196), msg, attr(0)))
    elif level == None:
        pass




