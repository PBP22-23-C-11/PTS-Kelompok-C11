release: sh -c 'python manage.py migrate && python manage.py collectstatic'
web: gunicorn project_django.wsgi --log-file -