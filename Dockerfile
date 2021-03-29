 FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 ADD requirements.txt /code/
 RUN pip install -r requirements.txt
 ADD . /code/

#  RUN python manage.py collectstatic --noinput

#  CMD gunicorn todo_list.wsgi:application --bin 0.0.0.0:$PORT
 