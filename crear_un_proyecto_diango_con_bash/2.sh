#!bin/bash
nombre_proyecto=$1
nombre_app=$2

if [ -z ${nombre_proyecto} ] || [ -z ${nombre_app} ]; then

   echo "*******************************************"
   echo "USO : bash 2.sh nombre_proyecto nombre_app "
   echo "*******************************************"
   echo "*******************************************"

else
 django-admin startproject "${nombre_proyecto}_project" . 
 python manage.py startapp "${nombre_app}_app" 
 python manage.py migrate
 python manage.py runserver

fi

