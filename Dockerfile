FROM python

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /web

COPY . /web/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8000
