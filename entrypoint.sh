python manage.py makemigrations  --noinput
python manage.py makemigrations incidents --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
daphne -b 0.0.0.0 -p 8000 incident_tracker.asgi:application
