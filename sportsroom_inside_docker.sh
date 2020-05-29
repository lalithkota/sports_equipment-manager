# exit_func() {
#         echo "SIGTERM detected"
#         exit 1
# }
# trap exit_func SIGTERM SIGINT

# Run the celery beat is taking in, as arg, its own schedule-DB. So use this inside docker only.
# That schedule-DB will be mounted at this given point. So it doesnt give problem there.
# But when the script is run normally, it might try to create that file in your local machine and create problems.
./redis-server&
celery -A sportsroom worker -l info &
celery -A sportsroom beat -l info -s /myDb/sportsRoom-celerybeat-schedule &
python manage.py makemigrations
python manage.py migrate
python manage.py $@
