	# Project-LoCatr
Web app for CNG Status and locator

## Aim
Develop an web app that would help users find status of CNG gas stations. 

## Current architecture:

 _Backend_   : Python -> *Django* Framework  
 _Database_  : MySQL  
 _UI_        : Bootstrap   
   
## Hosting 
 
 Heroku Platform

## setup the project locally

### Hosting requirements 
(same on windows and linux)
* git (installed using installer)
* Python 2.7
* virtualenv (only on linux)
	* you can use "pip" that comes with python installer (setup_location/Scripts/pip) to install virtualenv
	* comand to install virtualenv using pip is "pip install virtualenv"

### Steps to host it locally for Windows

* git clone https://github.com/scifiswapnil/Project-LoCatr.git
* pip install -r requirements.txt
* cd LoCatr
* python manage.py runserver (in browser you can open localhost:8000)

### Steps to host it locally for Linux

* git clone https://github.com/scifiswapnil/Project-LoCatr.git
* source bin/activate
* pip install -r requirements.txt
* cd LoCatr
* python manage.py runserver (in browser you can open localhost:8000)
* after use run "deactivate"

### folders/files description : (basic only for UI)
* /requirements.txt : for environment packages setup
* /LoCatr (folder) : django app
* /LoCatr/manage.py : django start app file
* /LoCatr/db.sqlite3 : local database
* /LoCatr/LoCatr/templates : html pages
* /LoCatr/LoCatr/static/js : js pages
* /LoCatr/LoCatr/static/css : css pages


