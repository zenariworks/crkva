FROM python:3.9-alpine3.13
LABEL maintainer="zenari.io"

ENV PYTHONBUFFERED=1

COPY ./requirements.txt /requirements.txt
COPY ./crkva /app
COPY ./scripts /scripts

WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client freetype-dev

RUN apk add --update --no-cache --virtual .tmp-deps \
    libffi-dev build-base postgresql-dev musl-dev linux-headers git && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps

RUN adduser --disabled-password --no-create-home app && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/static/media && \
    chown -R app:app /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:${PATH}"

USER app

CMD ["run.sh"]
