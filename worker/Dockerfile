FROM python:3.10-slim

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt update -y && \
    apt upgrade -y && \
    rm -rf /var/cache/apt/* && \
    rm -rf /var/lib/apt/lists/*

ADD ./requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

RUN useradd -mU worker
USER worker

COPY app/ /usr/src/app
WORKDIR /usr/src/app/

CMD ["python", "__main__.py"]
# CMD ["sleep", "infinity"]
