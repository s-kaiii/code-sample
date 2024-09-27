install:
	python3 -m venv venv
	venv/bin/pip3 install --upgrade pip &&\
	venv/bin/pip3 install -r requirements.txt

format:	
	venv/bin/black src/*.py

test:
	venv/bin/python3 -m pytest -vv --cov=src

lint:
	venv/bin/ruff check src/*.py

run:
	cat ./README.md.template > ./README.md
	venv/bin/python3 ./main.py
	echo "![graph](./output/predicted_vs_actual.png)" >> README.md

all: install lint test format run