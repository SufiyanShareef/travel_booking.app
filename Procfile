release: python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn travel_booking.wsgi