#############
# k8s setup #
#############

.PHONY: download-install-poetry
download-install-poetry:
	curl -sSL https://install.python-poetry.org/ | python -

# TODO: Pin to stable instead of preview once poetry 1.2 is released
poetry_setup: ## Setup virtual env and install dependencies
	deactivate || true
	poetry self update --preview || true
	poetry config virtualenvs.create true
	poetry config virtualenvs.in-project true
	poetry install --with dev --no-interaction -v
.PHONY: poetry_setup
