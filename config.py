import yaml
from pathlib import Path
from dotenv import load_dotenv
import os

class Config:
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.config_file = self.base_dir / "config" / "default.yaml"
        self.load_config()

    def load_config(self):
        load_dotenv()  # Load .env if exists
        
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                self.config = yaml.safe_load(f) or {}
        else:
            self.config = {}
            # Create default config if not exists
            self._create_default_config()

    def _create_default_config(self):
        default_config = {
            "templates": {
                "default": "fastapi-postgres"
            },
            "git": {
                "default_branch": "main",
                "enable_hooks": True
            },
            "logging": {
                "level": "INFO",
                "log_to_file": True
            }
        }
        self.config_file.parent.mkdir(exist_ok=True)
        with open(self.config_file, 'w') as f:
            yaml.dump(default_config, f, default_flow_style=False)
        self.config = default_config

    def get(self, key: str, default=None):
        """Get config value with dot notation (e.g., 'git.default_branch')"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            value = value.get(k, default) if isinstance(value, dict) else default
            if value is default:
                break
        return value

# Global config instance
config = Config()
