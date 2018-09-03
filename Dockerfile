FROM python:3.6-alpine

RUN apk update && apk add build-base postgresql-dev libffi-dev dumb-init bash
RUN pip install -U pip 

WORKDIR /code/

# ADD requirements-dev.txt /code/
# RUN pip install -r requirements-dev.txt

# ADD requirements.txt /code/
# RUN pip install -r requirements.txt

RUN pip install pipenv 
ADD Pipfile /code/
ADD Pipfile.lock /code/
RUN pipenv install --dev

ADD . /code/
RUN pipenv install -e .

ADD run /usr/local/bin/run
RUN chmod +x /usr/local/bin/run

ENTRYPOINT ["dumb-init", "pipenv", "run"]

CMD ["/usr/local/bin/run"]
