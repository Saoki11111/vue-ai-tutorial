FROM python:3.9.2-buster

ENV LANG C.UTF-8
ENV Tz Asia/Tokyo

COPY ./docker/python/requirements.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /app

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5001", "--reload"]
