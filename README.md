# DjongoPlayground

How to run the Django server 
1. Can execute the command line 'python manage.py runserver'
2. Simply click run button from the menu (short key "^ R")

How to add a new page
1. settings.py - make sure the templates folder has been explicitly specified
2. urls.py - configure the urlpatterns field
3. In templates folder, make sure the html page has been added
4. Create the python file which can be called when the route is typed

How to add a new Django app
1. Go to the terminal, use the command line 'python manage.py startapp'
2. In PyCharm, navigate to Tools, find 'Run manage.py Task', and use the command 'startapp' followed by the app name
3. Go to settings.py, search for the variable 'INSTALLED_APPS', and add the configuration file of the Django app

How to register the new models that has been created with Django app
1. navigate to the admin.py and register the model with admin.site.register

How to create your model in the database (i.e. the db.sqlite3)
1. After you created the app, and the models in the Django app
2. Run the command line 'python manage.py makemigrations'. You may need to run 'python3 manage.py makemigrations'
3. Alternative: go to 'Tools' -> Run manage.py Task, then type 'makemigrations'
This make migration is used to create a mapping file in python. In order to create the table in the db,
you need to run 'migrate'

How to add data into your db?
1. Run command 'python3 manage.py createsuperuser', then give a username and password
2. Navigate to http://127.0.0.1:8000/admin/login/?next=/admin/ and login with your username and password
3. Navigate to the relevant table and then add rows in the tables

How to pass the object to the rendering page?
1. Navigate to the relevant view page (.py page)
2. In the render method, not only pass the name of the html page, but also the parameter.
The parameter is a dictionary with all the data from the db
3. In the html page, use add the code to loop through the objects and echo the content

Important:
Everytime when you change the model, you need to migrate it to the database
Run the command 'python3 manage.py makemigrations' to ensure the db create the table correctly

How to use image field in PyCharm
1. Install pillow
2. Go to your model class and use the 'ImageField' to upload your images
3. In setting.py file, define the media url and media root
4. add these to urlpatterns by appending static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
5. In order to display the image on the website, you need to add a <img> tag, the source is the url of the image

How to manage your packages for a project
1. Navigate to the option 'PyCharm' and select 'Preferences' (This is different for Windows System)
2. Select your project and then select 'Project Interpreter'
3. Click the '+' button to install a new package
4. You can select specific version for the new added package