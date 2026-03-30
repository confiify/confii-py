"""Confii: A flexible configuration management library for Python applications.

Confii provides a unified interface for loading, merging, and accessing
configuration values from multiple sources with support for environment-specific
configs, dynamic reloading, and hook-based transformations.
"""

import logging
import os
from typing import Optional

from confii.config import Config
from confii.config_builder import ConfigBuilder, builder
from confii.exceptions import (
    ConfigAccessError,
    ConfigFormatError,
    ConfigLoadError,
    ConfigMergeConflictError,
    ConfigNotFoundError,
    ConfigValidationError,
    ConfiiError,
)

# Async support (optional)
try:
    from confii.async_config import (
        AsyncConfig,
        AsyncHTTPLoader,
        AsyncLoader,
        AsyncYamlLoader,
    )

    HAS_ASYNC = True
except ImportError:
    HAS_ASYNC = False
    AsyncConfig = None  # type: ignore
    AsyncLoader = None  # type: ignore
    AsyncYamlLoader = None  # type: ignore
    AsyncHTTPLoader = None  # type: ignore

__version__ = "0.0.1"
__all__ = [
    "Config",
    "ConfigAccessError",
    "ConfigBuilder",
    "ConfigFormatError",
    "ConfigLoadError",
    "ConfigMergeConflictError",
    "ConfigNotFoundError",
    "ConfigValidationError",
    "ConfiiError",
    "builder",
    "setup_logging",
]

# Add async exports if available
if HAS_ASYNC:
    __all__.extend(["AsyncConfig", "AsyncHTTPLoader", "AsyncLoader", "AsyncYamlLoader"])


def setup_logging(level: Optional[str] = None) -> None:
    """Configure logging for the confii library.

    Call this explicitly if you want confii log output.
    Libraries should not configure logging by default — that is the
    application's responsibility.

    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL).
              If not provided, uses the CONFII_LOG_LEVEL environment
              variable or defaults to WARNING.
    """
    log_level = level or os.environ.get("CONFII_LOG_LEVEL", "WARNING")

    # Configure the logger for this package
    logger = logging.getLogger("confii")
    logger.setLevel(getattr(logging, log_level.upper()))

    # Only add handler if one doesn't exist (to avoid duplicates)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    # Prevent propagation to root logger to avoid duplicate messages
    logger.propagate = False


# Library best practice: add NullHandler to avoid "No handler found" warnings.
# Users who want log output should call setup_logging() explicitly.
logging.getLogger("confii").addHandler(logging.NullHandler())
