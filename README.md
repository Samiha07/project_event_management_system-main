
### Project Description:
This is an open source event management system built with Python3 and Django web framework.This is actually Event Organizing Planner Application. This is a general purpose django-app for syncing events planning to a local database and adding socialize event plans into the content to a website.

This was specifically designed to put events for one Socialize/Hangouts groups onto their independent website. However, it was designed to give flexibility to the developer for whatever SOCIALIZE APPLICATION content syncing and posting they wish.


### Technologies used :
#### Frontend:

 *  Here I had pick a JS/CSS for the front end and use Django Page Templates.

#### Backend:

 * Python Django and Django Rest Framework
 * Python version: Python 3.8.10
 * Django version: 3.1.4
 * Uses SQLite as the database


⌨️  Creating a Blank Django Project :
```
    sudo django-admin startproject django_forms
```
To Run the Application in Server :
```
    python manage.py runserver
    python3 manage.py runserver
```
 * Starting development server at,
 ```
    http://127.0.0.1:8000/
```
⌨️  Setup in VS Code Text Editor :
 * You can install Python or Django Extension in your vs code.

⌨️  Project Settings :
This command will migrate all our database in to SQLite3 file.
```
    python manage.py migrate
    OR,
    python3 manage.py migrate
```

⌨️  Built-In Components :
 * In the Chrome or Any browser to navigate into django admin panel check this url and it will show django administration,
```
   http://127.0.0.1:8000/admin/login/?next=/admin/
```
 * Create your user Id in Django Administration, run this command:
```
  python manage.py createsuperuser
  OR,
  python3 manage.py createsuperuser
```
 * Next Log In with your user ID and Password and the Dashboard will show you in this url,
 ```
    http://127.0.0.1:8000/admin/
```
⌨️  Working with Apps : URLs & Views

 * While working on app we can need multiple django templates so we can use this command

```
 python3 manage.py startapp socialize
```

###  Getting Started with Templates :
⌨️  Static Files & taking initial mark in the Django Template Language

 * To check the new template which we created we can see in the browser,
```
  http://127.0.0.1:8000/socialize/
```
 * To create Static site we need to add its bases styles UI.

⌨️  Key Django Template Language Features & Tags

⌨️  Adding a Detail Page

⌨️  Dynamic Paths : Dynamic URLs in Templates

⌨️  Using Django Template Inheritance
 * By creating custom templates of the app structure and applying the UI of the app front end


⌨️  Using Models

 * To work in model go to models.py file to create your app model.Make sure we added our project name in our forms setting.py file in installed app section.
 * To Create a database run this command,
 ```
    python manage.py makemigrations
    or,
    python3 manage.py makemigrations
```

 * If we want to execute the database of django we can run this command to migrate our database,
 ```
    python manage.py migrate
    or,
    python3 manage.py migrate
 ```
⌨️  Using the Admin Panel & Querying Data

⌨️  Adding Image Upload & Serving & Displaying Images

 * To adding images to upload it in the UI we can install this package which is called Pillow,
```
   python3 -m pip install Pillow
```
To check your uploaded image in browser you can go into this link, for example,
```
   http://127.0.0.1:8000/files/images/download.jpeg
```
You can now see the preview of your image
⌨️  Configuring the Admin Area

⌨️  More Socialize Fields & Outputting Related Data

⌨️  Render Data from the Database with a Model

⌨️  Creating a Modelform

⌨️  Handling Form Submission

⌨️  More on Form Submission & Validation

⌨️  From Modelform to Form

⌨️  Optimizing URLs



