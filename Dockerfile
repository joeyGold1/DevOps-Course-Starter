FROM python:3.12.3-alpine as base
    RUN pip install poetry
    WORKDIR /app
    ENTRYPOINT ["poetry", "run", "flask", "run", "--host=0.0.0.0"]
    COPY poetry.lock ./
    COPY pyproject.toml ./
    RUN poetry install

FROM base as development
    ENV FLASK_DEBUG=true
    EXPOSE 5000

FROM base as production
    ENV FLASK_DEBUG=false
    COPY todo_app ./todo_app
    EXPOSE 5000
