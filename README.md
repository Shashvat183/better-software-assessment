# Better Software Assessment

This repository contains my solution scaffold for the Better Software engineering assessment.

Scope:
- Task 1: Flask backend APIs for comments CRUD on a given task, plus automated tests (pytest).
- Task 2 (bonus): React frontend interface for tasks CRUD leveraging the existing template structure.

Assumptions:
- The official Flask+React template repo will be integrated subsequently; for now, a minimal scaffold is provided to begin Task 1 in isolation.
- In-memory storage is used temporarily for comments to enable test-driven development; persistence can be added following the template’s patterns.

Structure:
- backend/ — Flask app and tests
- frontend/ — placeholder; will align with the template

Getting started (backend):
1. Create a virtualenv (optional): `python -m venv .venv` then `./.venv/Scripts/Activate.ps1`
2. Install deps: `pip install -r backend/requirements.txt`
3. Run tests: `pytest -q`
