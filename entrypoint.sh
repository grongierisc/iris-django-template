#!/bin/sh

# start iris
/iris-main "$@" &

# wait for iris to be ready
/usr/irissys/dev/Cloud/ICM/waitISC.sh

# init iop
iop --init

# load production
iop -m /irisdev/app/app/interop/settings.py

# start production
iop --start Python.Production --detach

#run npm run build in the frontend
cd /irisdev/app/app/frontend

npm install

npm run build

# Move to the app directory
cd /irisdev/app/app

# python manage.py flush --no-input
python3 manage.py migrate
# create superuser
export DJANGO_SUPERUSER_PASSWORD=SYS
python3 manage.py createsuperuser --no-input --username SuperUser --email admin@admin.fr

# load demo data
python3 manage.py loaddata community/fixtures/demo.json

# collect static files
python3 manage.py collectstatic --no-input --clear

# open log in stdout
iop --log