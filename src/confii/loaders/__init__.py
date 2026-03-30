"""Configuration loaders for Confii.

This module provides loader classes for loading configuration from various
sources including files (YAML, JSON, TOML, INI), environment variables,
and remote sources (HTTP, cloud storage, Git).

Available Loaders
-----------------

File Loaders:
    - YamlLoader: Load from YAML files (.yaml, .yml)
    - JsonLoader: Load from JSON files (.json)
    - TomlLoader: Load from TOML files (.toml)
    - IniLoader: Load from INI files (.ini, .cfg)

Environment Loaders:
    - EnvironmentLoader: Load from system environment variables

Remote Loaders:
    - HTTPLoader: Load from HTTP/HTTPS URLs
    - S3Loader: Load from AWS S3
    - SSMLoader: Load from AWS SSM Parameter Store
    - AzureBlobLoader: Load from Azure Blob Storage
    - GCPStorageLoader: Load from Google Cloud Storage
    - IBMCloudObjectStorageLoader: Load from IBM Cloud Object Storage
    - GitLoader: Load from Git repositories

Example:
    >>> from confii.loaders import YamlLoader, EnvironmentLoader
    >>> from confii import Config
    >>>
    >>> config = Config(loaders=[YamlLoader("config.yaml"), EnvironmentLoader("APP")])
"""

from confii.loaders.env_file_loader import EnvFileLoader
from confii.loaders.environment_loader import EnvironmentLoader
from confii.loaders.ini_loader import IniLoader
from confii.loaders.json_loader import JsonLoader
from confii.loaders.loader import Loader
from confii.loaders.remote_loader import (
    AzureBlobLoader,
    GCPStorageLoader,
    GitLoader,
    HTTPLoader,
    IBMCloudObjectStorageLoader,
    RemoteLoader,
    S3Loader,
)
from confii.loaders.ssm_loader import SSMLoader
from confii.loaders.toml_loader import TomlLoader
from confii.loaders.yaml_loader import YamlLoader

__all__ = [
    "AzureBlobLoader",
    "EnvFileLoader",
    "EnvironmentLoader",
    "GCPStorageLoader",
    "GitLoader",
    "HTTPLoader",
    "IBMCloudObjectStorageLoader",
    "IniLoader",
    "JsonLoader",
    "Loader",
    "RemoteLoader",
    "S3Loader",
    "SSMLoader",
    "TomlLoader",
    "YamlLoader",
]
