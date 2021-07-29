# Pull the base image with python 3.8 as a runtime for your Lambda
FROM public.ecr.aws/lambda/python:3.8

COPY requirements.txt ./

# Install the python requirements from requirements.txt
RUN python3.8 -m pip install -r requirements.txt

# COPY model_weights/ ./model_weights/

# Set the CMD to your handler
CMD ["app.lambda_handler"]