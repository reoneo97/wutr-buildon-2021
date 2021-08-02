# Pull the base image with python 3.8 as a runtime for your Lambda
FROM python:3.8-slim-buster

COPY requirements.txt ./

# Install the python requirements from requirements.txt
RUN pip3 install -r requirements.txt

COPY model_weights/ ./model_weights/