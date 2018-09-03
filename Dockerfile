FROM python:3.6-alpine

RUN apk update && apk add build-base postgresql-dev libffi-dev dumb-init bash
RUN pip install -U pip 

WORKDIR /code/

ADD requirements-dev.txt /code/
RUN pip install -r requirements-dev.txt

ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD . /code/
RUN pip install -e .

ADD run /usr/local/bin/run
RUN chmod +x /usr/local/bin/run

ENTRYPOINT ["dumb-init"]

CMD ["/usr/local/bin/run"]
