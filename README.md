# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## Dependencies
The first thing you will need to do to run the app is clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup.
```bash
$ cp .env.template .env
```

### Trello Dependencies
To run the app, you will need to:
1. Create a Trello account
2. Create an API Key for Trello
 - Create a Trello Power Up (https://trello.com/power-ups/admin)
 - Generate a new API key (shows as an option after creating the Power Up)
3. Create a API Token for Trello from the “Token” link on the page where your API key is displayed:
4. Create a board
5. Create 3 lists on the board
6. Open dev tools and view network requests. Filter by 'lists'
7. View the response to the request at /1/board/...
8. Copy the id (as board id) and from lists, copy the id of each list
9. Enter all of these into your .env file

## Running the App Using Docker (Recommended)
The above dependencies are sufficient for running the app in a Docker Container using the instructions below:
### For local development
Using these instructions will give you debug logs and code changes appearing without having to rebuild the image.
1. To build the development image, run:
```bash
$ docker build --target development --tag todo-app:dev .
```
2. To run the development image, run:
```bash
$ docker run --env-file ./.env -p 8080:5000 --mount "type=bind,source=$(pwd)/todo_app,target=/app/todo_app" todo-app:dev
```

The app should then be accessible at localhost:8080

### For a deployed production environment

1. To build the production image, run
```bash
$ docker build --target production --tag todo-app:prod .
```
2. To build the production image, run
```bash
$ docker run --env-file <ENV FILE LOCATION> -p 80:5000 todo-app:prod
```

## System Requirements If Not Using Docker
If you cannot use Docker, continue reading to see the rest of the instructions.

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

You can check poetry is installed by running `poetry --version` from a terminal.

**Please note that after installing poetry you may need to restart VSCode and any terminals you are running before poetry will be recognised.**

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app 'todo_app/app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 113-666-066
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running tests
The entire test suite can be run within the poetry environment by running
```bash
$ poetry run pytest
```

Individual test suites can be run by running
```bash
$ poetry run pytest <PATH_TO_TEST>
```

## CI
On pushing to github, on opening a pull request, and every Friday lunchtime, a github actions pipeline that runs the tests and checks for vulnerabilities will be run.

## Deployments

### Initial deployment
To deploy the app to Azure app service for the first time:
1. Build the container image: 
```bash
$ docker build --target production --tag joeygold/todo-app:prod .
```
2. Push the image to docker:
```bash
$ docker push joeygold/todo-app:prod
```
3. Create an app service plan
```bash
$ az appservice plan create --resource-group cohort32-33_JoeGol_ProjectExercise --name JoeGol-todo-app-plan --sku B1 --is-linux
```
4. Create an Azure webapp specifying the container image
```bash
$  az webapp create --resource-group cohort32-33_JoeGol_ProjectExercise --plan JoeGol-todo-app-plan --name JoeGol-todo-webapp --deployment-container-image-name docker.io/joeygold/todo-app:prod
```
5. Set the environment variables. If you have a local env file in .env notation that you would like to use, you can use the script below to convert it to json. `.deployment-env` is a useful template:
```bash
$ ./envJsonConverter.sh {yourEnvFileName} env.json
```
If using secrets, these should be stored in the key vault and referenced in the environment variables as: `@Microsoft.KeyVault(VaultName=myvault;SecretName=mysecret)`. If only using data that can be checked into source control, `env.json` can be replaced by another file name as it is included in `.gitignore`.


Set the config from `env.json` in Azure.
```bash
$ az webapp config appsettings set --resource-group cohort32-33_JoeGol_ProjectExercise --name JoeGol-todo-webapp --settings "@env.json"
```

### Future deployments
To update the deployed app:
1. Build the container image: 
```bash
$ docker build --target production --tag joeygold/todo-app:prod .
```
2. Push the image to docker:
```bash
$ docker push joeygold/todo-app:prod
```
4. If the environment variables should change, these should be updated by Azure CLI or manually. If you have a local env file in .env notation that you would like to use, you can use the script below to convert it to json. `.deployment-env` is a useful template:
```bash
$ ./envJsonConverter.sh {yourEnvFileName} env.json
```
If using secrets, these should be stored in the key vault and referenced in the environment variables as: `@Microsoft.KeyVault(VaultName=myvault;SecretName=mysecret)`. If only using data that can be checked into source control, `env.json` can be replaced by another file name as it is included in `.gitignore`.

Set the config from `env.json` in Azure.
```bash
$ az webapp config appsettings set --resource-group cohort32-33_JoeGol_ProjectExercise --name JoeGol-todo-webapp --settings "@env.json"
```
3. Call the POST webhook to trigger Azure to restart the app and pull the latest version of the image from the docker container regsitry. The webhook URL can be found in the deployment centre on the Azure web portal.
```bash
$ curl -X POST '{webhook_url}'
```

The deployed site can be accessed at: https://joegol-todo-webapp.azurewebsites.net/
