#!/usr/bin/python3
''' compresses a folder and performs
    a full deployment to remote servers
'''
from fabric.api import *
from datetime import datetime
from os.path import isfile
env.hosts = ['35.243.153.36', '35.237.150.213']


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


def do_deploy(archive_path):
    ''' deploy static files to the web_servers '''
    if not isfile(archive_path):
        return False
    file_name = archive_path.split('/')[1].split('.')[0]
    deploy_path = "/data/web_static/releases/" + file_name
    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(deploy_path))
        run("tar -xvzf /tmp/{}.tgz -C {}".format(file_name, deploy_path))
        run("rm /tmp/{}.tgz".format(file_name))
        run("mv {}/web_static/* {}".format(deploy_path, deploy_path))
        run("rm -rf {}/web_static".format(deploy_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(deploy_path))
        return True
    except Exception:
        return False


def deploy():
    ''' creates and distributes an archive to your web servers '''
    path_created_file = do_pack()
    if path_created_file is None:
        return False
    return do_deploy(path_created_file)
