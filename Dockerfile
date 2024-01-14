# start docker with linux kernal + install python 3.11
FROM python:3.11.6-slim-bullseye

# update kernal + install libraries 
RUN apt-get update && apt-get -y install gcc libpq-dev 

# create folder project 
WORKDIR /app

# copy requ.txt to app
COPY requirements.txt /app/requirements.txt

# install 
RUN pip install -r /app/requirements.txt
