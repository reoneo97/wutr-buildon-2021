FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

EXPOSE 8000
WORKDIR /usr/app
COPY . .
RUN pip install --upgrade pip
RUN pip3 install -r backend/requirements.txt

CMD ["uvicorn","main:app","--reload","--host","0.0.0.0","--port","8000"]