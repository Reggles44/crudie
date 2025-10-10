FROM python:3.11-slim AS base

WORKDIR /app
COPY Pipfile Pipfile.lock /app/

RUN pip install pipenv
RUN pipenv install --dev --system --deploy

COPY app.py .

EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8888", "app:app"]
