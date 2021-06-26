FROM python:3.7.6

RUN pip install discord
RUN pip install requests
WORKDIR /app

ADD . /app/

CMD [ "python", "./main.py" ]