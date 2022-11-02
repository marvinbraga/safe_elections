FROM python:3.10-slim as venv

RUN : \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        build-essential \
        binutils  \
        gettext \
    && :

RUN python -m venv /venv
ENV PATH=/venv/bin:$PATH

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt


FROM python:3.10-slim

RUN : \
    && apt-get update \
    && apt-get clean \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        python3-dev  \
        build-essential  \
        gettext  \
        openssh-server  \
        openssh-client  \
        libssl1.1 \
    && rm -rf /var/lib/apt/lists/* \
    && :

COPY . /code/

WORKDIR /code

ENV PATH=/venv/bin:$PATH \
    PYTHONOPTIMIZE=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=app.settings

COPY --from=venv /venv /venv

COPY ./.docker/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

RUN mkdir -p staticfiles && python manage.py collectstatic --noinput

RUN useradd --create-home local_user
USER local_user

ENTRYPOINT ["/entrypoint"]