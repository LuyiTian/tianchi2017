"""Configure path and dependency."""

import os


USER_NAME = os.uname()[1]

if USER_NAME == 'Dajuns-MacBook-Pro.local':
    BASE_PATH = '/Users/luodajun/Documents/workspace/tianchi2017'
elif USER_NAME == 'LuyiTians-MacBook-Pro.local':
    BASE_PATH = '/Users/luyi/data/tianchi2017/'
elif USER_NAME == '':
    BASE_PATH = ''
elif USER_NAME == '':
    BASE_PATH = ''  # aliyun linux server
else:
    raise Exception('Invalid Machine Name %s' % USER_NAME)