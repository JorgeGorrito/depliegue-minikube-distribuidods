FROM python:slim

WORKDIR /usr/app/

COPY . .

RUN python3 -m pip install -r requirements.txt

CMD python3 manage.py runserver 0:3000