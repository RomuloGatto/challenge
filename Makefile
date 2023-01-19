.PHONY: help
help: ## Show help.
	@printf "A set of development commands.\n"
	@printf "\nUsage:\n"
	@printf "\t make \033[36m<commands>\033[0m\n"
	@printf "\nThe Commands are:\n\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\t\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: setup
setup: ## Setup poetry environment
	poetry shell
	poetry install

.PHONY: test
test: ## Run tests locally
	poetry run pytest --cov=src --color=yes tests/

.PHONY: lint pre-commit
lint | pre-commit: ## Run the pre-commit config
	poetry run pre-commit run -a

.PHONY: requirements
requirements: ## Export requirements file based on poetry packages
	poetry export -f requirements.txt --output requirements.txt --without-hashes
