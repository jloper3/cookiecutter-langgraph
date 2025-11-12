# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Setup

```bash
uv venv
uv add langgraph=={{ cookiecutter.langgraph_version }}
uv add langgraph-sdk=={{ cookiecutter.langgraph_sdk_version }}
uv add langchain-core{{ cookiecutter.langchain_core_version }}
uv add -e ".[dev]"
```

## Usage

```bash
python -m {{ cookiecutter.package_name }}.agent
```

## Testing

```bash
pytest --cov={{cookiecutter.package_name}}
```
