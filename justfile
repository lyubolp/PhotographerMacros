venv:
    . .venv/bin/activate

init:
    python3 -m venv .venv
    venv
    pip install -r requirements.txt

lint: venv
    python3 -m pylint src/* --fail-under 9
    mypy src --ignore-missing-imports

test: venv
    python3 -m unittest discover -s tst

push: venv lint test
    git push

coverage: venv
    coverage run --source="src" -m unittest discover -s tst 
    coverage report -m --fail-under 75 --include="src/*" --sort=cover --skip-empty

run: venv
    python3 src/main.py