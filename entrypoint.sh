#!/bin/sh

# start iris
/iris-main "$@" &

# wait for iris to be ready
/usr/irissys/dev/Cloud/ICM/waitISC.sh

# init iop
# iop --init

# # load production
# iop -m /irisdev/app/src/python/iop/settings.py

# # start production
# iop --start Python.Production