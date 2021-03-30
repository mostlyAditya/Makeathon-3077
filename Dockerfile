FROM python:alpine
COPY . /project
WORKDIR /project
RUN apk add --update --no-cache g++ gcc libxslt-dev
RUN pip install -r requirements.txt
RUN python manage.py migrate
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000
