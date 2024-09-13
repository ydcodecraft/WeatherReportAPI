FROM python:3.10-slim

WORKDIR /code

# copy and install dependencies in docker
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt


# copy alembic for database migration
COPY ./alembic /code/alembic
COPY ./alembic.ini /code/alembic.ini

# copy core
COPY ./app /code/app

# expose the port for fastapi
EXPOSE 8000