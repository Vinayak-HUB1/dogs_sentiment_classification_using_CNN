FROM python:3.6.5

COPY . /src

WORKDIR /src

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["uvicorn","app.main:app","--host=0.0.0.0","--reload"]

