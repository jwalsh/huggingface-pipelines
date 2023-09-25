# Default value for POSTGRES_PASSWORD if not provided in the environment
POSTGRES_PASSWORD ?= setenvironmentpassword

.PHONY: postgres stop_postgres remove_postgres deps venv activate help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


postgres: ## Run PostgreSQL Docker container
	docker run -d --name hugging-postgres -e POSTGRES_PASSWORD="$(POSTGRES_PASSWORD)" -p 5432:5432 postgres

stop_postgres: ## Stop the PostgreSQL Docker container
	docker stop hugging-postgres

remove_postgres: ## Remove the PostgreSQL Docker container
	docker rm hugging-postgres

deps: ## Install dependencies using Homebrew
	@echo "Installing dependencies..."
	brew install jq libpq

venv: ## Create a virtual environment and install dependencies
	@echo "Creating virtual environment..."
	python3 -m venv venv

	@echo "Activating virtual environment..."
	source venv/bin/activate && pip install -r requirements.txt

	@echo "Virtual environment setup complete."

requirements.txt: venv ## Freeze dependencies to requirements.txt
	@echo "Freezing dependencies to requirements.txt..."
	pip freeze > requirements.txt

activate: ## Activate the virtual environment
	@echo "Activating virtual environment..."
	source venv/bin/activate
