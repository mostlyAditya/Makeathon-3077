FROM python:alpine
COPY . /project
WORKDIR /project
RUN apk add --update --no-cache g++ gcc libxslt-dev
RUN pip install -r requirements.txt
RUN python manage.py runserver
