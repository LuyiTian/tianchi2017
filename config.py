"""Configure path and dependency."""

import os


USER_NAME = os.uname()[1]

if USER_NAME == 'Dajuns-MacBook-Pro.local':
    BASE_PATH = '/Users/luodajun/Documents/workspace/tianchi2017'
    DATA_PATH = os.path.join(BASE_PATH, 'dataset')
elif USER_NAME == '':
    BASE_PATH = ''
elif USER_NAME == '':
    BASE_PATH = ''
else:
    raise Exception('Invalid Machine Name %s' % USER_NAME)