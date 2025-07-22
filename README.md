## Developer Guide

### Dependencies

This repository uses [uv](https://docs.astral.sh/uv/) for project management. Dependency bounds are defined in [`pyproject.toml`](pyproject.toml) and the locked environment is specified in [`uv.lock`](uv.lock).

```
uv sync
```

# Model/Analysis

This repository contains a single analysis script [`aviation.py`](aviation.py), which implements a simple model for global aviation. It outputs the required global fleet.

To execute the analysis script, run:

```
uv run python aviation.py
```

### Documentation

This repository uses Mkdocs to generate a static documentation site. The contents of the site can be found in [`docs/`](docs).

To serve the site locally, run:

```
uv run mkdocs serve
```
