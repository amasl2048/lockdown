FROM python:3.9.10-alpine as python-flask

RUN pip3 install flask gunicorn Flask-HTTPAuth

# Stage 2
FROM python-flask

WORKDIR /home/app

RUN mkdir -p ./static

COPY ./static/*.png ./static/
COPY ./templates ./templates
COPY ./*.py ./

EXPOSE 8002

CMD ["gunicorn", "--bind", "0.0.0.0:8002", "start_web_server:app"]
