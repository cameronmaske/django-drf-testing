FROM python:3.6-alpine

RUN apk update && apk add build-base postgresql-dev libffi-dev dumb-init bash
RUN pip install -U pip 

WORKDIR /app/

RUN pip install pipenv 
ADD Pipfile /app/
ADD Pipfile.lock /app/
ADD setup.py /app/
RUN pipenv run python setup.py develop
RUN pipenv install --dev

ADD . /app/

ADD run /usr/local/bin/run
RUN chmod +x /usr/local/bin/run

ENTRYPOINT ["dumb-init", "pipenv", "run"]

CMD ["/usr/local/bin/run"]
