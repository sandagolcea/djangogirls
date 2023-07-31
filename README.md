
## App from Django Girls

Django girls walkthrough of a simple blog post application.
Tutorial can be found [here](https://tutorial.djangogirls.org/en).

Application to show and add to a list of _blog_ posts.

_Geolocation_ to show you the country/city you're connecting from. You will need to install requests for this app, as I've not put them in requirements.txt

`$ pip install requests`

Point covered include:
 - (blog) a form to add posts
 - iterating over a list of posts
 - displaying several views (list view, form and post detail)
 - using a base template
 - adding a model for the posts that are saved in the db
 - (geolocation) making an API request and displaying received data

### To start this app:
  - Pre-req (from requirements.txt):
    - `pip install -r requirements.txt`
    - (geolocation): `$ pip install requests`
  - Activate virtual env:
    - `source .venv/bin/activate`
  - Make all db migrations:
    - `python manage.py makemigrations blog`
    - `python3 manage.py migrate`
  - Run server
    - `python manage.py runserver`
