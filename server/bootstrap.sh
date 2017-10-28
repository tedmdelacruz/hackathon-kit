#!/bin/bash

# Wait for db service to be ready using netcat
nc -z db 3306
n=$?
while [ $n -ne 0 ]; do
    sleep 1
    nc -z db 3306
    n=$?
done

python3 manage.py runserver 0.0.0.0:8000
