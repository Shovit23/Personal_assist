from database import get_name
import os

name = get_name()



def is_linux():

    if 'Linux' in str(os.uname()):
        return True

    else:
        return False
    

