FROM python:3.10-slim

ENV PYTHONBUFFERED 1

RUN useradd -mU worker
USER worker

ADD ./requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

WORKDIR /usr/src/worker

CMD ["python", "app/__main__.py"]
