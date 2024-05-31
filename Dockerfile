FROM python:3.12.3-alpine as base
    RUN pip install poetry
    WORKDIR /app
    COPY poetry.lock ./
    COPY pyproject.toml ./
    RUN poetry install

FROM base as development
    ENV FLASK_ENV development
    ENTRYPOINT ["poetry", "run", "flask", "run", "--host=0.0.0.0"]
    EXPOSE 5000

FROM base as production
    COPY todo_app ./todo_app
    ENTRYPOINT ["poetry", "run", "flask", "run", "--host=0.0.0.0"]
    EXPOSE 5000:5000

    
