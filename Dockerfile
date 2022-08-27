FROM python:3.6.5


COPY . /app


WORKDIR /app


RUN pip install --upgrade pip


RUN pip install -r requirements.txt


EXPOSE $PORT


CMD gunicorn -k uvicorn.workers.UvicornWorker app:app

