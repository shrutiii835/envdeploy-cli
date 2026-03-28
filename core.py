import subprocess
from pathlib import Path
from envdeploy.logger import logger

def run_bash_script(script_path: str, *args) -> bool:
    try:
        script = Path(script_path)
        if not script.exists():
            logger.error(f"Script not found: {script}")
            return False

        logger.info(f"Executing: {script.name}")
        result = subprocess.run([str(script)] + list(args), capture_output=True, text=True, check=True)

        if result.stdout:
            print(result.stdout.strip())
        if result.stderr:
            logger.warning(result.stderr.strip())

        logger.success(f"✅ {script.name} executed successfully")
        return True

    except subprocess.CalledProcessError as e:
        logger.error(f"Script failed (exit {e.returncode})")
        if e.stdout: print(e.stdout)
        if e.stderr: logger.error(e.stderr)
        return False
    except Exception as e:
        logger.error(f"Error: {e}")
        return False

def setup_git(project_path: str, project_name: str) -> bool:
    return run_bash_script("scripts/git_setup.sh", project_path, project_name)

def setup_environment(project_path: str, project_name: str) -> bool:
    return run_bash_script("scripts/setup_project.sh", project_path, project_name)
