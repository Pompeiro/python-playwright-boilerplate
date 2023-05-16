FROM ubuntu:jammy

RUN apt update
RUN apt install -y python3.11 python3.11-venv
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1

RUN apt-get update && apt-get install -y \
    curl \
    gcc
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -

WORKDIR /app
COPY . .
RUN POETRY_VIRTUALENVS_CREATE=false /root/.local/bin/poetry install --no-root

RUN playwright install chromium && playwright install firefox && playwright install-deps

ENV PYTHONPATH "${PYTHONPATH}:/app/"
