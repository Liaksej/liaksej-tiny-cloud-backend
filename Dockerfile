# pull official base image
FROM python:3.12-slim

LABEL authors="liaksej"

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

# create the app user
RUN addgroup --system app && adduser --system --group app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install curl and pip then install poetry
RUN apt-get update && \
    apt-get install --no-install-recommends -y curl netcat-openbsd gcc && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    rm -rf /var/lib/apt/lists/*

# Make sure scripts in .local are usable:
ENV PATH=$HOME/.local/bin:$PATH

# Copy only requirements to cache them in docker layer
COPY ./poetry.lock ./pyproject.toml /home/app/web/

# preventive measure to ignore creating a virtualenv within another one
RUN poetry config virtualenvs.create false

# Project initialization:
RUN poetry add gunicorn
RUN poetry install --no-root

# copy project
COPY . $APP_HOME

# run entrypoint.sh
RUN chmod +x $APP_HOME/entrypoint.sh
RUN chown -R app:app $APP_HOME
USER app
CMD /bin/sh -c "${APP_HOME}/entrypoint.sh"
