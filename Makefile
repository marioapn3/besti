start:
	uvicorn app.main:app --reload --port 8081

install:
	pip install -r requirements.txt

uninstall:
	pip uninstall -r requirements.txt

start_venv:
	source env/bin/activate

seeders:
	python -m app.db.seeders.run_seeders

	