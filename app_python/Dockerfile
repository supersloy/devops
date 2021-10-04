FROM python:3.8-slim-buster
WORKDIR app_python

COPY . .
RUN pip install -r requirements.txt && adduser appusr
USER appusr

EXPOSE 10101
CMD ["python","main.py"]