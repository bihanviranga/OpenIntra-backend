# OpenIntra-backend

## Installation instructions
- Clone the repository and cd into the folder.
- Create a virtual environment `python -m virtualenv venv`
- Activate it. `source venv/bin/activate`
- Install requirements. `pip install -r requirements.txt`
- Migrate the database `python manage.py migrate`
- Run the server `python manage.py runserver`
- [OPTIONAL] Create a superuser account: `python manage.py createsuperuser`

