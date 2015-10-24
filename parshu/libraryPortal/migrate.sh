rm db.sqlite3
rm -rf portal/migrations
python manage.py syncdb
./runserver.sh
