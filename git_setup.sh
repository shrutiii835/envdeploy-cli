#!/bin/bash
# =============================================
# envdeploy - Git Setup Module (Final v3)
# Robust Git initialization - commit before branching
# =============================================

set -euo pipefail

PROJECT_DIR="${1:-.}"
PROJECT_NAME="${2:-unknown-project}"

cd "$PROJECT_DIR" || { echo "Error: Cannot access project directory $PROJECT_DIR"; exit 1; }

echo "🔧 Setting up professional Git workflow for: $PROJECT_NAME"

# Initialize Git if not already a repository
if [ ! -d ".git" ]; then
    git init
    echo "✅ Git repository initialized"
else
    echo "ℹ️  Git repository already exists"
fi

# Suppress master warning globally
git config --global init.defaultBranch main 2>/dev/null || true

# Ensure we start on main
git checkout -B main

# Create .gitignore first
if [ ! -f ".gitignore" ]; then
    cat > .gitignore << 'EOL'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual Environments
venv/
ENV/
env/
.venv/
.env

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Logs
logs/
*.log

# Testing
.coverage
htmlcov/
.tox/
.nox/
.cache
.pytest_cache/
EOL
    echo "✅ Created professional .gitignore"
fi

# Set local Git config
git config user.name "envdeploy User"
git config user.email "dev@local"
echo "✅ Set local Git user config"

# Add files and make FIRST commit on main (critical step)
git add .
if ! git diff --cached --quiet; then
    git commit -m "chore: initial commit by envdeploy-cli

- Project scaffolded automatically with envdeploy-cli
- Professional Git workflow setup (main + develop)
- Comprehensive .gitignore for Python projects" 
    echo "✅ Initial commit created on main branch"
else
    echo "ℹ️  No changes to commit"
fi

# Now safely create develop branch from main (after commit exists)
if ! git show-ref --verify --quiet refs/heads/develop; then
    git branch develop
    echo "✅ Created 'develop' branch from main"
else
    echo "ℹ️  'develop' branch already exists"
fi

# Final status
echo "🎉 Git setup completed successfully!"
echo "   Current branch : $(git branch --show-current)"
echo "   Branches       : $(git branch --format='%(refname:short)' | tr '\n' ' ' | xargs)"
echo "   Latest commit  : $(git log --oneline -n 1)"
