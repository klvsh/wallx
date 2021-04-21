init:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt

lint:
	autopep8 --in-place --aggressive --recursive *.py elements
	pylint *.py elements

clean:
	find elements -name "*.pyc" -exec rm -rf {} \;
	find elements -name "*.pyo" -exec rm -rf {} \;
	find elements -name "__pycache__" -exec rm -rf {} \;

run:
	python main.py
