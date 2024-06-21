#!/bin/sh

# start iris
/iris-main "$@" &

# wait for iris to be ready
/usr/irissys/dev/Cloud/ICM/waitISC.sh

# Move to the app directory
cd /irisdev/app/app

# python manage.py flush --no-input
python3 manage.py migrate
# create superuser
export DJANGO_SUPERUSER_PASSWORD=admin
python3 manage.py createsuperuser --no-input --username admin --email admin@admin.fr

# load demo data
python3 manage.py loaddata community/fixtures/demo.json

# init iop
iop --init

# load production
iop -m /irisdev/app/app/interop/settings.py

# start production
iop --start Python.Production