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
