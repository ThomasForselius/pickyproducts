# pickyproducts
Django project CMS for CRUD operations regarding PickyFrame

# Installing Django
# Reading and Showing products from db
# Adding products to db
# Updating products in db
# Deleting product from db


## Install Django: 

These are the installing and deployment steps for starting and running a Django project:

- pip3 install 'django<4' / to get the latest verion before 4, since 4 is not long term supported
- 'django-admin startproject pickyproducts .'  / starts a new django project with the name 'pickyproducts'
- 'python3 manage.py startapp productsadmin' / starts a new django app with the name 'productsadmin'
- 'python3 manage.py runserver' / starts the django server
- 'python3 manage.py migrate' / creates basic databases
- 'python3 manage.py createsuperuser' / creates superuser
- Create/update db model in *models.py* / this is where you design your model structure
- 'python3 manage.py makemigrations' / sets up new model for db, ready for migration
- 'python3 manage.py migrate' / creates new migration in db
- Open admin.py and add: 
    - 'from models import Product' / Note: 'Product' is the name of the table created in *models.py*
    - 'admin.site.register(Product)'

## Showing items from db: 

- In *views.py* , add a new class using the following lines:
    - def show_prod(request):
        products = Product.objects.all()
        context = {
            'products' : products
        }
        return render(request, 'admin/show_prod.html', context)

        *the variable 'products' is what you use to show products in show_prod.html, by using a for-loop to iterate through*.
        
        *i.e. {% for product in products %}*

- In *urls.py*, add the following information: 
    - 'from productsadmin.views import show_prod' / *show_prod* is the name of the class defined in *views.py*
    - in urlpatterns, add the following:
        - 'path('', show_prod, name='show_prod')

- Now go to your local server and add '/admin' in the address field to access admin panel
- Login using the superuser credentials you created earlier
- Under the Users table, Products should appear
- To make added items display names instead of 'Item #number' in products table the following line has to be added to *models.py*:
    -  def __str__(self):
        return self.name

- In the file show_prod.html, use this code to iterate through the dictionary of items imported from the view.py file:
    -  {% for product in products %} 
    - now in this for-loop you can use *product.name, product.id, product.price and so on to display eache key value*

## Adding items to db:

To add items to the database you need to add a frontend page by following these steps:

- in the /templates/admin/ folder, add a new page called "show_prod.html"
- In 'urls.py', add the following information behind *from productsadmin.views import show_prod*: 
    - 'add_prod' / 'add_prod' is the name of the class defined in 'views.py'
    - in urlpatterns, add the following:
        - 'path('add', add_prod, name='add_prod')
- In *views.py* add the following:
    - def add_prod(request):
    return render(request, 'admin/add_prod.html')
- In 