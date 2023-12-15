# pull official base image
FROM python:3.12-slim

LABEL authors="liaksej"

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install curl and pip then install poetry
RUN apt-get update && \
    apt-get install --no-install-recommends -y curl && \
    curl -sSL https://install.python-poetry.org | python -

# Make sure scripts in .local are usable:
ENV PATH=/root/.local/bin:$PATH

# Copy only requirements to cache them in docker layer
COPY ./poetry.lock ./pyproject.toml /usr/src/app/

# preventive measure to ignore creating a virtualenv within another one
RUN poetry config virtualenvs.create false

# Project initialization:
RUN poetry install --no-dev


# Uncomment this line If you want to run container as non-root user
RUN groupadd app && useradd -g app app

COPY . /usr/src/app

# run entrypoint.sh
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*
RUN chmod +x /usr/src/app/entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
USER app
