FROM python:3.8-slim-buster
WORKDIR app_python

COPY . .
RUN ["pip", "install", "-r", "requirements.txt"]

CMD ["python","main.py"]