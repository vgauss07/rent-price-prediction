.PHONY: run install clean check runner
.DEFAULT_GOAL:=runner

run: install
	cd src; poetry run python3 runner.py

install: pyproject.toml
	poetry install 

clean:
	rm -rf `find . -type d -name __pycache__`
	rm -rf .qodo

check:
	poetry run flake8 src/

runner: run clean
