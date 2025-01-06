FROM python:3.12.3-alpine AS base
    RUN pip install poetry
    WORKDIR /app
    COPY poetry.lock pyproject.toml ./
    RUN poetry install

FROM base AS development
    ENV FLASK_DEBUG=true
    EXPOSE 5000
    ENTRYPOINT ["poetry", "run", "flask", "run", "--host=0.0.0.0"]


FROM base AS production
    ENV FLASK_DEBUG=false
    COPY todo_app ./todo_app
    EXPOSE 5000
    ENTRYPOINT ["poetry", "run", "flask", "run", "--host=0.0.0.0"]

FROM base AS test
    COPY todo_app ./todo_app
    ENTRYPOINT ["poetry", "run", "pytest"]
