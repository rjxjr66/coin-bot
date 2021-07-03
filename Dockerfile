FROM python:3.7.6

RUN pip install discord
RUN pip install requests
RUN pip install redis
WORKDIR /app

COPY . /app/

CMD [ "python", "./main.py" ]