import typer
from rich.console import Console
from envdeploy.logger import logger
from envdeploy.core import setup_git, setup_environment
from pathlib import Path

console = Console()

app = typer.Typer(
    name="envdeploy",
    help="Automated Environment & Deployment CLI",
    add_completion=True,
)

@app.command()
def version():
    """Show version information"""
    console.print("╭──────────────────────────────────────╮")
    console.print("│ envdeploy-cli v0.1.0                 │")
    console.print("│ Built with ❤️  for DevOps            │")
    console.print("╰──────────────────────────────────────╯")

@app.command()
def new(project_name: str = typer.Argument(..., help="Name of the new project")):
    """Create a new project with automated setup"""
    console.print(f"🚀 Creating [bold cyan]{project_name}[/bold cyan]")

    project_path = Path(project_name)
    project_path.mkdir(exist_ok=True)

    # Git Setup
    console.print("🔧 Setting up Git workflow...")
    setup_git(str(project_path.absolute()), project_name)

    # Environment Setup
    console.print("🐍 Setting up Python environment...")
    setup_environment(str(project_path.absolute()), project_name)

    console.print(f"\n🎉 [bold green]Project {project_name} is ready![/bold green]")
    console.print(f"   cd {project_name}")
    console.print("   source venv/bin/activate")
    console.print(f"   uvicorn {project_name.replace('-', '_')}.main:app --reload")

def main():
    """Entry point for the CLI (required by pyproject.toml)"""
    app()

if __name__ == "__main__":
    main()
