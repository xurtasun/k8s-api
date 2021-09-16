FROM python:3.9.5-alpine

COPY ./src/ /data/user/
WORKDIR /data/user/

RUN /usr/local/bin/pip install -r /data/user/requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]
