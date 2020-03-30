FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3 python3-pip libpq-dev gettext
COPY . /curaSWISS-backend
WORKDIR /curaSWISS-backend
RUN pip3 install -r requirements.txt
RUN pip3 install -r requirements.prod.txt

CMD python3 manage.py runserver 0.0.0.0:$PORT
