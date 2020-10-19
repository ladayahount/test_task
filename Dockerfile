FROM python:3.7

RUN pip install fastapi uvicorn sqlalchemy

EXPOSE 80

COPY ./app /app
COPY ./app /main
COPY ./app /__init__
COPY ./app /crud
COPY ./app /database
COPY ./app /models
COPY ./app /ring.db
COPY ./app /schemas
COPY ./app /test_main



CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]