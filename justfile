venv:
    . .venv/bin/activate

init:
    python3 -m venv .venv
    venv
    pip install -r requirements.txt

lint: venv
    python3 -m pylint src/* --fail-under 9
    mypy src --ignore-missing-imports
    flake8 src

test: venv
    python3 -m unittest discover -s tst

push: venv lint test
    git push

coverage: venv
    coverage run -m unittest discover -s tests
    coverage report -m --fail-under 75

run: venv
    python3 src/main.py