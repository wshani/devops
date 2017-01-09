FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY . /app
WORKDIR /app
RUN pip install -r /app/foobar/requirements.txt

#EXPOSE 5000

VOLUME /data

CMD python -m foobar
