
.PHONY: lint test format all

# Lint the code using flake8
lint:
	flake8 src tests

# Run unit tests with pytest
test:
	pytest --cov=src

# Format the code using black
format:
	black src tests

# Run all the checks (lint, test, format)
all: lint test format
