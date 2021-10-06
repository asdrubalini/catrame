FROM python:3.9-slim

RUN useradd -mU api
USER api

ADD ./requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

WORKDIR /usr/src/api/

CMD ["python", "app/"]
