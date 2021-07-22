.ONESHELL:

lint:
	prospector

mypy:
	mypy src

test:
	python -m unittest
