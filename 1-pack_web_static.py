#!/usr/bin/python3
# fabric module
from datetime import datetime
from fabric.api import local
from fabric import task


@task
def do_pack():
    """script that generates a .tgz archive from the contents
    of the web_static folder of this repository.
    """

    d = datetime.now()
    now = d.strftime('%Y%m%d%H%M%S')

    local("mkdir -p versions")
    local("tar -czvf versions/web_static_{}.tgz web_static".format(now))
