# Python-Preparations

## Poetry
poetry init
poetry shell
deactivate
poetry add <packet>
poetry install

The VSCode Python settings are configured to use local .venv:
Poetry is configured to create virtualenvs in project:
To complete the setup:
add to user settings for vscode

```
"python.venvPath": "${workspaceFolder}/.venv"
"terminal.integrated.env.osx": {
    "POETRY_VIRTUALENVS_IN_PROJECT": "true"
}```

Delete the existing virtualenv:
```poetry env remove python```

Create new virtualenv in project:

```poetry config virtualenvs.in-project true```

```poetry install```



This will create the .venv folder in your project directory. Then use Python: Select Interpreter command in VS Code to select the Python interpreter from the new .venv folder.