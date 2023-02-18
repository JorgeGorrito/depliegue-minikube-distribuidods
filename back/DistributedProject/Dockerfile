FROM python:3.12.0a5-alpine3.17

WORKDIR /usr/app/

COPY . .

RUN python3 -m pip install -r requirements.txt

EXPOSE 8000

CMD python3 manage.py runserver 0:8000 --settings=DistributedProject.settings.local