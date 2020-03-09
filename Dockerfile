FROM python:3.7

LABEL Description="Query AWS account for an infrastructure information"
LABEL Version = "0.2"

# Project Files and Settings
ARG PROJECT=app
ARG PROJECT_DIR=/app

RUN mkdir -p $PROJECT_DIR
WORKDIR $PROJECT_DIR
COPY . $PROJECT_DIR

RUN pip install -r requirements.txt

# Server
EXPOSE 8000
STOPSIGNAL SIGINT
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]