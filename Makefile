.ONESHELL:

lint:
	prospector

mypy:
	mypy src tests

test:
	python -m unittest

cov:
	coverage run -m unittest
	coverage report
	coverage html
