FROM python:3.12-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PIP_NO_CACHE_DIR 1

WORKDIR /app

COPY . /app
COPY ./conf/gunicorn/gunicorn.conf.py /etc/gunicorn/gunicorn.conf.py

RUN pip install --upgrade pip && \
    pip install --no-cache-dir --upgrade -r requirements.txt && \
    python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "core.wsgi:application", "-c", "/etc/gunicorn/gunicorn.conf.py"]