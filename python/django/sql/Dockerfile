FROM python:3.11-slim as base

WORKDIR /app
COPY Pipfile Pipfile.lock /app/

RUN pip install pipenv
RUN pipenv install --system --deploy

###

FROM base as develop

RUN pipenv install --dev --system --deploy

COPY manage.py ./
COPY crudie crudie/

EXPOSE 8000
CMD ["./manage.py", "runserver", "0.0.0.0:8000"]
