"""Configuration validators for Confii.

This module provides validation capabilities for configurations using
Pydantic models and JSON Schema.

Available Validators
--------------------

- SchemaValidator: Validates configurations against JSON Schema
- PydanticValidator: Validates configurations using Pydantic BaseModel classes

Example:
    >>> from confii.validators import PydanticValidator
    >>> from pydantic import BaseModel
    >>>
    >>> class AppConfig(BaseModel):
    ...     database_url: str
    ...     port: int = 8080
    >>>
    >>> validator = PydanticValidator(AppConfig)
    >>> validated = validator.validate(config_dict)
"""

from .pydantic_validator import PydanticValidator
from .schema_validator import SchemaValidator

__all__ = ["PydanticValidator", "SchemaValidator"]
