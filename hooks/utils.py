import os
from distutils.spawn import find_executable


DEBUG = os.environ.get('DEBUG', False)

def which(command):
    result = find_executable(command)
    if DEBUG:
        print('which %s' % command)
        print(result)
    if result is None:
        print('ERROR: %s is required but not found' % command)
    return result
