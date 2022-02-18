#!/bin/bash -x

PWD=`pwd`
activateVirtualEnvironment () {
    . $PWD/.venv/bin/activate
}

echo $PWD

createVirtualEnvironment () {
    python3 -m venv .venv
    activateVirtualEnvironment
    python3 -m pip install --upgrade pip
}

poetryInstallUpdateList () {
    poetry install
    poetry update
    poetry show
}

if [ ! -d '.venv' ]; then
    echo "Creating .venv folder"
    rm -r '.venv'
    createVirtualEnvironment

else
    echo "Deleting existing .venv folder"
    rm -r '.venv'
    createVirtualEnvironment
fi

if [ ! -f 'poetry.lock' ]; then
    echo "Creating new poetry.lock ..."

else
    rm 'poetry.lock'
fi

if [ ! -f 'pyproject.toml' ]; then
    echo "Creating new pyproject ..."
    touch pyproject.toml
    echo '[tool.poetry]
          name = "backed_mobile"
          version = "1"
          description = ""
          authors = ["Urbvan Tech <tech@urbvan.com>"]

          [tool.poetry.dependencies]
          python = "*"

          [tool.poetry.dev-dependencies]
          pytest = "^3.4"' >> pyproject.toml
    poetryInstallUpdateList
    printf '\e[1;34;6mProject dependencies are ready\n'


else
    rm "poetry.lock"
    poetryInstallUpdateList
    printf '\e[1;34;6mProject dependencies are ready\n'
fi