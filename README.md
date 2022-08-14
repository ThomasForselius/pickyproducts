# pickyproducts
Django project CMS for CRUD operations regarding PickyFrame


## Install Django: 

These are the installing and deployment steps for starting and running a Django project:

- pip3 install 'django<4' / to get the latest verion before 4, since 4 is not long term supported
- 'django-admin startproject pickyproducts .'  / starts a new django project with the name 'pickyproducts'
- 'python3 manage.py startapp productsadmin' / starts a new django app with the name 'productsadmin'
- 'python3 manage.py runserver' / starts the django server
- 'python3 manage.py migrate' / creates basic databases
- 'python3 manage.py createsuperuser' / creates superuser
- Create/update db model in models.py / this is where you design your model structure
- python3 manage.py makemigrations / sets up new model for db, ready for migration
- python3 manage.py migrate / creates new migration in db
- Open admin.py and add: 
    - 'from models import Product' / Note: 'Product' is the name of the table created in models.py
    - 'admin.site.register(Product)'

- Now go to your local server and add '/admin' in the address field to access admin panel
- Login using the superuser credentials you created earlier
- Under the Users table, Products should appear

- To make added items display names instead of 'Item #number' in products table the following line has to be added to models.py:
    -  def __str__(self):
        return self.name

