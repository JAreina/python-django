#!bin/bash
nombre_proyecto=$1

nombre_app=$2


echo ${nombre_proyecto}

if [ -n ${nombre_proyecto} ]; then
 django-admin startproject "${nombre_proyecto}_project" . 
fi
if [ -n ${nombre_app} ]; then
 python manage.py startapp "${nombre_app}_app" 
 python manage.py migrate
fi

if [ -n ${nombre_proyecto} ] &&  [ -n ${nombre_app} ] ;then
 python manage.py runserver
fi
