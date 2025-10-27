# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

Project overview
- Backend: Flask API in backend/app with an application factory and a single blueprint providing task comment endpoints. State is in-memory (module-level dicts), so restarting the server resets data.
- Frontend: frontend is a placeholder for a future React UI (see frontend/README.md).

Common commands
Environment setup
```bash path=null start=null
# Unix-like shells
python -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
```
```powershell path=null start=null
# Windows PowerShell
python -m venv .venv
. .venv\Scripts\Activate.ps1
pip install -r backend/requirements.txt
```

Run tests
```bash path=null start=null
# All tests
pytest -q backend
# Single test
pytest -q backend/tests/test_comments_api.py::test_add_edit_delete_comment
# By pattern
pytest -q backend -k "404"
```

Run the backend API (Flask app factory)
```bash path=null start=null
# From the backend/ directory
python -m flask --app app:create_app run --port 5000 --debug
# The API base URL will be http://localhost:5000/api
```

High-level architecture
- Application factory: backend/app/__init__.py defines create_app() which constructs the Flask app and registers routes via register_routes.
- Routing and domain: backend/app/routes.py defines a Blueprint named "api" mounted at /api. Endpoints:
  - POST /api/tasks/<int:task_id>/comments → create a comment (JSON body: {"text": string}).
  - PUT/PATCH /api/tasks/<int:task_id>/comments/<int:comment_id> → update text.
  - DELETE /api/tasks/<int:task_id>/comments/<int:comment_id> → delete.
  Comments are stored in in-memory dicts COMMENTS and NEXT_ID.
- Tests: backend/tests/test_comments_api.py uses pytest with a fixture that builds the app via create_app() and exercises add/edit/delete flows and 404s.
- Frontend: frontend/README.md notes that the React UI will come later; backend is currently self-sufficient for tests.

Notes for agents
- No linter/formatter/type-checker is configured in this repo. Prefer adding tools only when explicitly requested.
- There is no Docker or CI config; run locally using the commands above.
