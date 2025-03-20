FROM python:3-alpine

WORKDIR /app

COPY requirements.txt /tmp
COPY src/* /app/

RUN python -m pip install \
    --requirement /tmp/requirements.txt

ENTRYPOINT [ "python", "main.py" ]

CMD [ "--help" ]
