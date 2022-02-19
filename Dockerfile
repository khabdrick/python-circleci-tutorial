FROM python:3.8

RUN mkdir /flask-circleci
COPY requirements.txt /flask-circleci
ADD . /

WORKDIR /flask-circleci

EXPOSE 5000

CMD python main.py