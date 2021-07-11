FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

EXPOSE 8000
WORKDIR /usr/app

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .
CMD ["uvicorn","main:app","--reload","--host","0.0.0.0","--port","8000"]