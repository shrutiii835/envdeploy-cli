import logging
import sys
from pathlib import Path
from datetime import datetime

class EnvDeployLogger:
    def __init__(self, name: str = "envdeploy", log_to_file: bool = True):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        # Clear existing handlers to avoid duplicates
        if self.logger.handlers:
            self.logger.handlers.clear()
        
        # Console handler with rich formatting
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)
        
        # File handler (logs/ directory)
        if log_to_file:
            log_dir = Path("logs")
            log_dir.mkdir(exist_ok=True)
            log_file = log_dir / f"envdeploy_{datetime.now().strftime('%Y%m%d')}.log"
            
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.DEBUG)
            file_formatter = logging.Formatter(
                '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s'
            )
            file_handler.setFormatter(file_formatter)
            self.logger.addHandler(file_handler)
        
        self.logger.info("envdeploy logger initialized")

    def info(self, msg: str):
        self.logger.info(msg)
    
    def success(self, msg: str):
        self.logger.info(f"✅ {msg}")
    
    def warning(self, msg: str):
        self.logger.warning(msg)
    
    def error(self, msg: str):
        self.logger.error(msg)
    
    def debug(self, msg: str):
        self.logger.debug(msg)

# Global logger instance
logger = EnvDeployLogger()
