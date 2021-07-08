FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app
COPY . /app
RUN pip3 install -r backend/requirements.txt

CMD ["uvicorn","main:app","--reload","--host","0.0.0.0","--port","8000","--app-dir","./backend/"]