# Vendor-Management-System-
This project aims to develop a comprehensive Vendor Management System (VMS) to streamline the process of managing vendors, track purchase orders, and calculate vendor performance metrics.
## Prerequisites
* Python (version 3.x recommended)
* Django
* Django REST Framework
# Setup Instructions
## Create a Virtual Environment:
* python -m venv myenv 
* Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
* myenv\scripts\activate
## Install Dependencies:
* pip install django
* pip install djangorestframework
## Set up a new project
django-admin startproject VendorHub
cd VendorHub
django-admin startapp VendorConnect
## Database migration
* python manage.py makemigrations
* python manage.py migrate
## Superuser creation
* python manage.py createsuperuser
## Running the server
* python manage.py runserver
## Access Django Admin:
* Open the Django admin at http://127.0.0.1:8000/admin/ and log in using the superuser credentials. this is to access the database as a admin user.
## how to run a api endpoint:
* first we need to make sure that we migrated the models to database
* then we need to start the server using "python manage.py runserver" command.
* then we need to open another cmd prompt and open virtual environment and open the project folder.

