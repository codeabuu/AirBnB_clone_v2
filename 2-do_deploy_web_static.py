#!/usr/bin/python3
"""Compress web static package
"""
from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['52.86.139.197', '100.24.74.142']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/mykey'


def do_deploy(archive_path):
    """Deploy web files to server
    """
    try:
        if not (path.exists(archive_path)):
            return False

        # Upload archive
        put(archive_path, '/tmp/')

        # Create target dir
        timestamp = archive_path[-18:-4]
        target_dir = '/data/web_static/releases/web_static_{}/'.format(timestamp)
        run('sudo mkdir -p {}'.format(target_dir))

        # Uncompress archive
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C {}'.format(timestamp, target_dir))

        # Remove archive
        run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

        # Use rsync to move contents (recursively) into the host web_static
        run('sudo rsync -a /data/web_static/releases/web_static_{}/web_static/ {}'.format(timestamp, target_dir))

        # Remove source_dir
        run('sudo rm -rf {}/web_static/'.format(target_dir))

        # Delete pre-existing symbolic link
        run('sudo rm -rf /data/web_static/current')

        # Re-establish symbolic link
        run('sudo ln -s {} /data/web_static/current'.format(target_dir))
    except:
        return False

    # Return True on success
    return True

