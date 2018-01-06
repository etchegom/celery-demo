FROM python:3-alpine

RUN mkdir /app
VOLUME /app

COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt && rm -f /requirements.txt

WORKDIR /app
CMD ["python", "stresser.py"]
