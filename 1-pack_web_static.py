#!/usr/bin/python3
''' compresses a folder '''
from fabric.api import *
from datetime import datetime


def do_pack():
    ''' method that compresses
        files to a .tgz format
    '''
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    local("mkdir -p versions/")
    try:
        local("tar -cvzf versions/web_static_{}.tgz web_static".format(date))
        return "versions/web_static_{}.tgz".format(date)
    except Exception:
        return None
