release: python manage.py migrate
web: gunicorn --chdir bedside bedside.wsgi:application