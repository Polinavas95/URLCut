FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# set work directory
RUN mkdir /backend
WORKDIR /backend/

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY pyproject.toml /backend/

# Allow installing dev dependencies to run tests
ARG DEBUG=true
RUN bash -c "if [ $DEBUG == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"

# RUN poetry install
ENV PYTHONPATH=/backend

COPY . /backend
