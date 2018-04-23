install:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock

clean:
	rm -rf .pytest_cache

lint:
	pipenv run flake8 --max-line-length=110

test: lint
	export PYTHONPATH=$(PWD) && pipenv run pytest src/test
