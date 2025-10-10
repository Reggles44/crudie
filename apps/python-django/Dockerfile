FROM python:3.11-slim AS base

WORKDIR /app
COPY Pipfile Pipfile.lock /app/

RUN pip install pipenv
RUN pipenv install --dev --system --deploy

COPY manage.py ./
COPY crudie crudie/

EXPOSE 8888
CMD ["./manage.py", "runserver", "0.0.0.0:8888"]
