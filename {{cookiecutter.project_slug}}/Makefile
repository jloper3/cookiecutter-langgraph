.PHONY: install lint format test clean

install:
	uv sync

lint:
	uv run ruff check .
	uv run mypy {{cookiecutter.package_name}}

format:
	uv run black .
	uv run isort .

test:
	uv run pytest --cov={{cookiecutter.package_name}} --cov-report=term-missing

clean:
	rm -rf dist build .pytest_cache *.egg-info
