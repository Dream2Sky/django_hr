#!/bin/bash

echo "removing old project"
rm -rf /root/web/django_hr

echo "copy new project to web"
/bin/cp -rf /var/lib/jenkins/workspace/django_hr /root/web/

echo "change to new project"
cd /root/web/django_hr || exit

PROCESS=$(ps -e | grep uwsgi | awk '{printf "%d\n", $1}')
for i in $PROCESS; do
  echo "Kill the uwsgi process [ $i ]"
  kill -9 $i
done
#
#CPROCESS=$(ps -e | grep celery | awk '{printf "%d\n", $1}')
#for i in $CPROCESS; do
#  echo "Kill the celery process [ $i ]"
#  kill -9 $i
#done
echo "finish kill"

export BUILD_ID=dontKillMe

source /root/.local/share/virtualenvs/django_hr-W5BZcG1I/bin/activate
/usr/local/bin/pipenv install --skip-lock
python manage.py migrate

cd /root/web/ || exit
nohup /urs/bin/uwsgi --ini uwsgi.ini

sleep 10s

#nohup celery -A imageprocessing worker -l info -P eventlet -c 1 >celery.out 2>&1 &
#
#sleep 10s

exit 0
