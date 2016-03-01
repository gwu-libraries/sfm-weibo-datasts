#!/bin/bash
echo "Updating packages"
apt-get install -y < /opt/sfm-weibo-datasts/requirements/requirements.apt

echo "Updating requirements"
pip install -r /opt/sfm-weibo-datasts/requirements/dev.txt --upgrade

echo "Waiting for db"
appdeps.py --wait-secs 30 --port-wait db:5432
if [ "$?" = "1" ]; then
    echo "Problem with application dependencies."
    exit 1
fi

echo "Syncing db"
/opt/sfm-weibo-datasts/weiboanalysis/manage.py syncdb --noinput

echo "Migrating db"
/opt/sfm-weibo-datasts/weiboanalysis/manage.py migrate --noinput

echo "Collecting static files"
/opt/sfm-weibo-datasts/weiboanalysis/manage.py collectstatic --noinput

echo "Running server"
/opt/sfm-weibo-datasts/weiboanalysis/manage.py runserver 0.0.0.0:80