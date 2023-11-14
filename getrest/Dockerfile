FROM python:3.8-slim

ENV FLASK_APP api.py

RUN pip install flask



WORKDIR /app


COPY getrest/api.py /app
COPY getrest/config.json /app


EXPOSE 5000


ENTRYPOINT ["flask","run","--host","0.0.0.0"]
