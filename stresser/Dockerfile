FROM python:3.6-alpine

RUN mkdir /app
VOLUME /app

COPY requirements.txt /
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt && rm -f /requirements.txt

ENV TIMER=100

WORKDIR /app
CMD ["python", "stresser.py"]
