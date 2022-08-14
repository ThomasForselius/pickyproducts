# pickyproducts
Django project CMS for CRUD operations regarding PickyFrame


## Install Django in terminal: 
- pip3 install 'django<4' to get the latest verion before 4, since 4 is not long term supported
- django-admin startproject pickyproducts .  / starts a new django project with the name 'pickyproducts'
- python3 manage.py startapp productsadmin / starts a new django app with the name 'productsadmin'
- python3 manage.py runserver / starts the django server
- python3 manage.py migrate / creates basic databases
- python3 manage.py createsuperuser / creates superuser
- create/update db model in models.py / this is where you design your model structure
- python3 manage.py makemigrations / sets up new model for db, ready for migration
- python3 manage.py migrate / creates new migration in db
