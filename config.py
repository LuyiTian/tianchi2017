"""Configure path and dependency."""

import os


USER_NAME = os.uname()[1]

if USER_NAME == 'Dajuns-MacBook-Pro.local':
    BASE_PATH = '/Users/luodajun/Documents/workspace/tianchi2017'
    DATA_PATH = os.path.join(BASE_PATH, 'dataset')
elif USER_NAME == 'LuyiTians-MacBook-Pro.local':
    BASE_PATH = '/Users/luyi/data/tianchi2017/'
    DATA_PATH = os.path.join(BASE_PATH, 'dataset')
elif USER_NAME == 'MacBook-pro':
    BASE_PATH = '/Users/bianbeilei/tianchi2017'
    DATA_PATH = os.path.join(BASE_PATH, 'dataset')
elif USER_NAME == 'WeAncestry.com':
    BASE_PATH = '/data/tianchi2017/'
    DATA_PATH = os.path.join(BASE_PATH, 'dataset')
else:
    raise Exception('Invalid Machine Name %s' % USER_NAME)
