# Testing Django Rest Framework

## Local development

### Running the server

To run the API, set up a `.env` file in the root directory of the project containing the following environment variables:

```bash
```

Then to start the server locally, run:

```bash
docker-compose up
```

The API would now be available at http://localdocker:5000 

#### Manage.py

```bash
docker-compose run api python manage.py <command>
```

### Running tests

To run tests locally, use the following command:

```bash
docker-compose run api pytest tests/
```

