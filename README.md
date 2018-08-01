# Testing Django Rest Framework

## Local development

### Running the server

Start the server locally by running:

```bash
docker-compose up
```

The API would now be available at http://<your-docker-ip-or-address>:5000 

#### Manage.py

```bash
docker-compose run api python manage.py <command>
```

### Running tests

To run tests locally, use the following command:

```bash
docker-compose run api pytest tests/
```

