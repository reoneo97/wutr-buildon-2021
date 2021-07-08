FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

EXPOSE 8000
WORKDIR /app
COPY . /app
RUN pip3 install -r backend/requirements.txt

ENTRYPOINT ["uvicorn","main:app","--reload","--host","0.0.0.0","--port","8000","--app-dir","./backend/"]