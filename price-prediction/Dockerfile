# Pull the base image with python 3.8 as a runtime for your Lambda
FROM public.ecr.aws/lambda/python:3.8


COPY requirements.txt ./

# Install the python requirements from requirements.txt
RUN pip3 install -r requirements.txt

#COPY model_weights/ ./model_weights/

COPY setup.py ./
RUN python setup.py
COPY app.py ./

# COPY model_weights/ ./model_weights/

CMD ["app.lambda_handler"]