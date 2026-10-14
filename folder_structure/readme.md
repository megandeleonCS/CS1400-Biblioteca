1. Recommended Python project structure
Here is a professional, modern starting point that works well for APIs, CLI tools, automation, and general Python applications.

text

my-project/
├── pyproject.toml
├── README.md
├── .gitignore
├── .env.example
├── src/
│   └── my_project/
│       ├── __init__.py
│       ├── main.py
│       ├── config.py
│       └── services/
│           ├── __init__.py
│           └── example.py
└── tests/
    ├── __init__.py
    └── test_example.py
What each file does:

pyproject.toml — project metadata, dependencies, build configuration, and tool settings.

src/my_project/main.py — application entry point.

src/my_project/__init__.py — marks the package and can remain empty.

config.py — configuration and environment-variable handling.

services/ — application logic organized by responsibility.

tests/ — automated tests.

README.md — setup, installation, and usage instructions.

.gitignore — prevents virtual environments, caches, secrets, and build artifacts from entering Git.

.env.example — documents required environment variables without exposing real credentials.

The src/ layout helps prevent accidental imports from your working directory instead of the installed package.

2. What should go inside main.py?
Keep it small. Its job is to start the application and coordinate the high-level flow—not to contain every function, database query, or business rule.

src/my_project/main.py

python

def main() -> None:
    """Run the application."""
    print("Application started")

    # Coordinate your application here.
    # Call functions from other modules as needed.


if __name__ == "__main__":
    main()
The if __name__ == "__main__": guard means main() runs when you execute the module directly, but not when another module imports it.

With this structure, you can run:

bash
python -m my_project.main
After installing the project in editable mode, Python can locate the package correctly.

My recommendation: use main.py for startup and orchestration. Put actual functionality into separate modules as the project grows.

3. Use pyproject.toml as the project configuration
This is the standardized modern configuration file for Python package metadata, build settings, and tool configuration. 

Python Packaging User Guide
+1

Here is a practical starting configuration using Hatchling as the build backend and pytest, Ruff, and mypy for development.

pyproject.toml

toml

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "my-project"
version = "0.1.0"
description = "A Python application"
readme = "README.md"
requires-python = ">=3.11"
dependencies = []

[dependency-groups]
dev = [
    "pytest",
    "ruff",
    "mypy",
]

[tool.hatch.build.targets.wheel]
packages = ["src/my_project"]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = ["--import-mode=importlib"]

[tool.ruff]
line-length = 88
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B"]

[tool.mypy]
python_version = "3.11"
strict = true
mypy_path = "src"
A few important details:

dependencies = [] is for runtime packages your application actually needs. Add dependencies there when needed.

The dev group keeps development tools separate from runtime dependencies.

Ruff handles linting, import sorting, and other code-quality checks.

mypy checks types; strict mode is useful but may require additional annotations.

Hatchling builds your package, while the explicit package path tells it where your code lives.

The dependency-group standard and packaging guide document this approach. 

Python Packaging User Guide
+1

This is a template, not a requirement to use every tool on every project.

4. Separate application logic into modules
For example, src/my_project/services/example.py might contain:

python

def greet(name: str) -> str:
    """Return a greeting for a user."""
    return f"Hello, {name}!"
Then src/my_project/main.py can use it:

python

from my_project.services.example import greet


def main() -> None:
    message = greet("Python developer")
    print(message)


if __name__ == "__main__":
    main()
Notice the import starts with my_project, not src.my_project. The src directory is the source root, not part of the Python package's import name.

As the project grows, add modules according to real responsibilities:

File or directory

Responsibility

main.py

Startup and orchestration

config.py

Environment and application configuration

models.py or models/

Data structures and domain models

services/

Business logic

repositories/

Data access, when needed

api/

HTTP endpoints, when building an API

utils/

Small, genuinely reusable helpers

Don't create all these directories automatically. Start with the pieces your project needs.

5. Add tests from the beginning
A real project should be easy to verify without manually running the entire application.

tests/test_example.py

python

from my_project.services.example import greet


def test_greet() -> None:
    assert greet("Alice") == "Hello, Alice!"
Because this uses a src/ layout, install the project in editable mode before running the tests. This is also the approach recommended by pytest's integration guidance. 

pytest documentation

6. Set up and run the project
I recommend starting with Python's built-in venv and pip. You can also use a modern project manager such as uv if you prefer managing environments and dependencies through one tool.

With venv and pip:

bash

# Create and enter the project directory
mkdir my-project
cd my-project

# Create a virtual environment
python -m venv .venv

# Activate it on macOS/Linux
source .venv/bin/activate

# On Windows PowerShell, use this instead:
# .venv\Scripts\Activate.ps1

# After creating your project files:
python -m pip install -e . --group dev

# Run the application
python -m my_project.main

# Run the tests
python -m pytest

# Check code quality
python -m ruff check .
python -m ruff format --check .
python -m mypy src/
The commands above assume your pyproject.toml and package files are already in place. The --group dev option requires a sufficiently recent pip version that supports dependency groups. 

Python Packaging User Guide
+1

7. Don't forget .gitignore
A good .gitignore prevents accidental commits of local environments, Python caches, and secrets.

text

.venv/
__pycache__/
*.py[cod]
.pytest_cache/
.mypy_cache/
.ruff_cache/
dist/
build/
*.egg-info/

.env
.env.*
!.env.example

.idea/
.vscode/
Keep .env.example in Git if it contains only placeholder values. Never commit actual API keys, passwords, or production credentials.

8. What else belongs in a production-ready project?
Add these as the project requires them:

README.md — how to install, configure, run, and test the project.

Type hints — make interfaces clearer and support static analysis.

Logging — use Python's logging module rather than relying on print() for operational messages.

CI — run tests and linting automatically when code is pushed or a pull request is opened.

Environment configuration — separate configuration from source code.

Dependency management — keep runtime and development dependencies distinct.

Error handling — handle expected failures deliberately; don't hide errors with broad exception handlers.

Documentation and security checks — add these when the project's complexity and deployment needs justify them.

You generally don't need a Dockerfile, database layer, requirements.txt, or multiple configuration files on day one. Add them when they serve a concrete purpose.

My final recommendation
For most new Python applications, start with these essentials:

pyproject.toml

Metadata, build system, dependencies, and tool configuration.

src/my_project/main.py

A minimal, clearly defined application entry point.

Modules and packages

Organize logic by responsibility instead of growing one giant file.

tests/

Automated checks from the start.

Git, .gitignore, and README.md

Version control, clean repositories, and reproducible setup instructions.