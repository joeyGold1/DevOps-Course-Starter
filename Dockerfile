FROM python:3.12.3-alpine as base
    RUN pip install poetry
    WORKDIR /app
    COPY poetry.lock pyproject.toml ./
    RUN poetry install

FROM base as development
    ENV FLASK_DEBUG=true
    EXPOSE 5000
    ENTRYPOINT ["poetry", "run", "flask", "run", "--host=0.0.0.0"]


FROM base as production
    ENV FLASK_DEBUG=false
    COPY todo_app ./todo_app
    EXPOSE 5000
    ENTRYPOINT ["poetry", "run", "flask", "run", "--host=0.0.0.0"]

FROM base as test
    COPY todo_app ./todo_app
    ENTRYPOINT ["poetry", "run", "pytest"]
