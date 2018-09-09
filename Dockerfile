FROM python:3.7-alpine
LABEL maintainer=dev@dschuldt.de

ADD app.py /app/
RUN apk add --no-cache tini && pip install bottle gunicorn

ENTRYPOINT ["sbin//tini", "--"]
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "--chdir", "/app", "app:app"]

