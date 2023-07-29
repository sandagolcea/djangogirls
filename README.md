
## App from Django Girls

Django girls walkthrough of a simple blog post application.
Tutorial can be found [here](https://tutorial.djangogirls.org/en).

Application to show and add to a list of blog posts.

Point covered include:
 - a form to add posts
 - iterating over a list of posts
 - displaying several views (list view, form and post detail)
 - using a base template
 - adding a model for the posts that are saved in the db

### To start this app:
  - Pre-req (from requirements.txt):
    - `pip install -r requirements.txt`
  - Activate virtual env:
    - `source .venv/bin/activate`
  - Make all db migrations:
    - `python manage.py makemigrations blog`
    - `python3 manage.py migrate`
  - Run server
    - `python manage.py runserver`
