SRC_DIR := src

.PHONY: build test test-coverage test-report

build: venv 
	. .venv/bin/activate && python src/folder_synchronizer.py

test: venv 
	. .venv/bin/activate && pytest -v

test-report: venv 
	. .venv/bin/activate && pytest -v --junitxml=test-results.xml

venv: .venv/touchfile

.venv/touchfile: $(SRC_DIR)/requirements.txt
	python3 -m venv .venv
	. .venv/bin/activate; pip install -Ur $(SRC_DIR)/requirements.txt
	touch .venv/touchfile
