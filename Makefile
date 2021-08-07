.ONESHELL:

lint:
	prospector

mypy:
	mypy src tests

test:
	python -m unittest
