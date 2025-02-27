lint:
	flake8 .

format:
	black .

check:
	mypy docbuilderpy/

test:
	pytest tests/

freeze:
	pip3 freeze > requirements.txt

install:
	pip3 install -r requirements.txt