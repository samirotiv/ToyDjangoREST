rm -rf portal/migrations
rm db.sqlite3
python manage.py syncdb
python manage.py runserver 0.0.0.0:8000
