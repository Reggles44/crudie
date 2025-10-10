FROM python:3.13-slim AS base

WORKDIR /app
COPY Pipfile Pipfile.lock /app/

RUN pip install -U pipenv 
RUN pipenv install --system --deploy

COPY app.py .

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8888", "app:app"]
