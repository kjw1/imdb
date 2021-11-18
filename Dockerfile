FROM python:3.9-alpine
WORKDIR /root

RUN apk add --no-cache openssl-dev libffi-dev python3-dev py3-cffi gcc musl-dev
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r /root/requirements.txt
COPY api.py .
COPY movies .
RUN rm -f /root/items.json && scrapy crawl imdb


ENV FLASK_APP=api
ENTRYPOINT ["flask", "run"]