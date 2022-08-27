FROM python:3.8.13


COPY . /app


WORKDIR /app


RUN pip install --upgrade pip


RUN pip install -r requirements.txt 


EXPOSE $PORT


CMD gunicorn -k uvicorn.workers.UvicornWorker app:app