FROM python:3.12.3-alpine
RUN pip install poetry

WORKDIR /app

COPY todo_app ./todo_app
COPY poetry.lock ./
COPY pyproject.toml ./
RUN poetry install

ENTRYPOINT ["poetry", "run", "flask", "run", "--host=0.0.0.0"]
EXPOSE 5000:5000

