# pickyproducts
Django project CMS for CRUD operations regarding PickyFrame

> 1. [What is it](#what-is-it)
> 2. [User Story](#user-story)
> 3. [UI & UX](#ui-&-ux)
> 4. [Installing Django](#install-django)
> 5. [Showing items from db](#showing-items-from-dbproducts)
> 6. [Adding Item to db](#adding-items-to-db)
> 7. [Updating Item in db](#updating-items-in-db)
> 8. [Deleting Item from db](#deleting-item-from-db)
> 9. [Testing](#testing)
> 10. [Deployment](#deployment)
> 11. [Tech](#technologies) 
> 12. [Support](#support)

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
    -   ```python
        def show_prod(request):
            products = Product.objects.all()
            context = {
                'products' : products
            }
            return render(request, 'admin/show_prod.html', context)
        ```
        *the variable 'products' is what you use to show products in show_prod.html, by using a for-loop to iterate through*.
        
        *i.e. {% for product in products %}*

- In *urls.py*, add the following information: 
    -   ```python
        from productsadmin.views import show_prod 
        ```  
        *show_prod* is the name of the class defined in *views.py*
    - in urlpatterns, add the following:
        -   ```python
                path('', show_prod, name='show_prod')
            ```

- Now go to your local server and add '/admin' in the address field to access admin panel
- Login using the superuser credentials you created earlier
- Under the Users table, Products should appear
- To make added items display names instead of 'Item #number' in products table the following line has to be added to *models.py*:
    -   ```python
            def __str__(self):
            return self.name
        ```

- In the file show_prod.html, use this code to iterate through the dictionary of items imported from the view.py file:
    -   ```python
        {% for product in products %} 
        ```
    - Now in this for-loop you can use *product.name, product.id, product.price and so on to display eache key value*

## Adding items to db:

To add items to the database you need to add a frontend page by following these steps:

- In *views.py* add the following:
    -   ```python
        def add_prod(request):
            if request.method == "POST": 
                name = request.POST.get("name")
                price = request.POST.get("price")
                desc = request.POST.get("desc")
                sale = 'sale' in request.POST
                sale_price = request.POST.get("sale_price")
                Product.objects.create(name=name, price=price, desc=desc, sale=sale, sale_price=sale_price)
                return redirect('show_prod')
        return render(request, 'admin/add_prod.html')
        ```
        This will define a function called add_prod
- In *urls.py*, add the following information behind *from productsadmin.views import show_prod*: 
    - add_prod / 'add_prod' is the name of the class defined in 'views.py'
    - in *urlpatterns*, add the following:
        -   ```python
                path('add', add_prod, name='add_prod')
            ```
- In the */templates/admin/* folder, create a new page called "add_prod.html"
- In the *add_prod.html* page, add your boilerplate html code and form with corresponding input fields to match your product model
- Now when you click sumbit, the field values will transfer to the views.py file and be inserted into the db
- You will then be redirected back to *show_prod.html* where the newly added product should appear

## Updating items in db

- In *views.py*, add the following information behind *render, redirect*: 
    -   ```python
            get_object_or_404
        ```
        *this function imports the product form the db using the prod_id as a primary key*
- In *views.py*, create a new function called edit_prod with the following code:
    ```python
    def edit_prod(request, prod_id): 
        prod = get_object_or_404(Product, id=prod_id)
        if request.method == "POST":
            name = request.POST.get("name")
            price = request.POST.get("price")
            desc = request.POST.get("desc")
            sale = 'sale' in request.POST
            sale_price = request.POST.get("sale_price")
            Product.objects.filter(pk=prod_id).update(name=name, price=price, desc=desc, sale=sale, sale_price=sale_price)
            return redirect('show_prod')
        context = {
            'name' : prod.name,
            'price' : prod.price,
            'desc' : prod.desc,
            'sale' : prod.sale,
            'sale_price' : prod.sale_price
        }
        return render(request, 'admin/edit_prod.html', context)
    ```
- In *urls.py*, add the following information behind *from productsadmin.views import show_prod, add_prod*: 
    -   ```python
        edit_prod
        ```
        *edit_prod* is the name of the class defined in 'views.py'
    - In the *urlpatterns* section, add the following: 
        - path('edit/<prod_id>', edit_prod, name='edit_prod') 
- To make sure that only the selected item in the db is updated, the following code must be added: 
    Product.objects.filter(pk=prod_id).update(name=name, price=price, desc=desc, sale=sale, sale_price=sale_price)
    - the *.filter(pk=prod_id)* part filters out a selected item to be updated via the *.update()* function that follows
- Create a new file called *edit_prod.html*. This wil be a clone of *add_prod.html*, but will populate the fields based on the data that is got from the db.
- To populate the corresponding input field, use the following codes:
    -   ```python
        {{ name }}
        ```
         *imports the value of name*
    -   ```python
        {{ price }}
        ```
        *imports the value of price*
    -   ```python
        {{ desc }}
        ````
        *imports the value of desc*
    -   ```python
        {{ sale_price }}
        ```
        *imports the value of sale_price*
    -   ```python
        {{ sale }}
        ````
        *imports the value of sale*
        
    - Since *sale* is a boolean function, the following if-loop will display a checked checkbox if sale equals True
        -   ```python
            {% if sale == True %}
            <input type="checkbox" id="sale" name="sale" checked>
            {% else %}
            <input type="checkbox" id="sale" name="sale" >
            {% endif %}
            ```

- Now when you click sumbit, the field values will transfer to the views.py file and be inserted into the db. 
- You will then be redirected back to *show_prod.html* where the newly added product should appear

## Deleting item from db