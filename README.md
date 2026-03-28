# envdeploy-cli

**Automated Development Environment Setup Tool**

A production-grade CLI that eliminates repetitive setup work for developers.

## Features
- `envdeploy new <project-name>` — Creates a complete FastAPI project in seconds
- Professional Git workflow (`main` + `develop` branches, proper `.gitignore`, initial commit)
- Automatic Python virtual environment creation
- Dependency installation with modern `pyproject.toml` + `src/` layout
- Structured logging and clean CLI interface

## Quick Usage

```bash
# Create new project
envdeploy new my-awesome-app

# Run the generated app
cd my-awesome-app
source venv/bin/activate
uvicorn my_awesome_app.main:app --reload
Open http://127.0.0.1:8000 to see the app running.
Technologies Used

Python — Typer (CLI), Rich (output), structured logging
Bash — Modular scripts for Git and environment setup
Git — Best practices automation
FastAPI + Uvicorn — Modern web framework template

Project Highlights

Clean modular architecture (Python orchestration + Bash execution)
Error handling and logging
Reproducible developer onboarding
Hybrid scripting approach commonly used in real DevOps tools

This project demonstrates practical DevOps skills: automation, tooling, and full environment lifecycle management.
Built as a portfolio project to showcase Python + Bash proficiency.
