FROM python:3.9 as base

COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip \
&& pip install -r /requirements.txt

FROM base

COPY . /app/

WORKDIR /app

CMD ["gunicorn", "--workers=2", "--chdir=.", "--bind", "0.0.0.0:5000", "--access-logfile=-", "--error-logfile=-", "app:app"]

