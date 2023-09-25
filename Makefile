POSTGRES_PASSWORD ?= setenvironmentpassword

.PHONY: postgres

postgres:
	docker run -d --name hugging-postgres -e POSTGRES_PASSWORD="$(POSTGRES_PASSWORD)" -p 5432:5432 postgres

stop_postgres:
	docker stop my-postgres

remove_postgres:
	docker rm my-postgres

deps:
	brew install jq
	brew install libpq

venv:
	@echo "Creating virtual environment..."
	python3 -m venv venv

	@echo "Activating virtual environment..."
	source venv/bin/activate

	@echo "Installing dependencies..."
	pip install -r requirements.txt

	@echo "Virtual environment setup complete."

requirements.txt:
	pip freeze > requirements.txt

activate:
	@echo "Activating virtual environment..."
	source venv/bin/activate
