import logging
from pathlib import Path


def configure_logger():
    """Return a logger that writes errors to the console and a log file."""
    logger = logging.getLogger("student_processor")
    logger.setLevel(logging.ERROR)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        project_folder = Path(__file__).resolve().parent.parent
        log_file = project_folder / "student_errors.log"
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
