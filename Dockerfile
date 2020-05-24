# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.8.2

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
# RUN mkdir /SportsRoom

# Set the working directory to /SportsRoom
# WORKDIR /SportsRoom

# Copy the current directory contents into the container at /SportsRoom
ADD . /SportsRoom

# Install any needed packages specified in requirements.txt
WORKDIR /SportsRoom
RUN /bin/bash redis_install_script.sh
WORKDIR /SportsRoom
RUN pip install -r requirements.txt

# EXPOSE 8000

# CMD ["/bin/bash", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
RUN python manage.py flush --noinput
RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', '', 'admin')" | python manage.py shell

ENTRYPOINT ["/bin/bash","sportsroom_inside_docker.sh", "runserver 0.0.0.0:8000"]
