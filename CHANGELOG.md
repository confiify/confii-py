# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project uses [Calendar Versioning](https://calver.org/) (`YYYY.MM.DD.MICRO`).

## [Unreleased]

### Added

- Initial release of Confii as a standalone package (migrated from config-stash)
- Multiple configuration sources: YAML, JSON, TOML, INI, .env, environment variables
- Cloud storage loaders: AWS S3, Azure Blob, Google Cloud Storage, IBM COS
- AWS SSM Parameter Store loader with pagination and decryption
- HTTP/HTTPS remote configuration loading
- Secret store integration: AWS Secrets Manager, HashiCorp Vault, Azure Key Vault, GCP Secret Manager
- HashiCorp Vault authentication: OIDC, LDAP, JWT, Kubernetes, AWS, Azure, GCP, AppRole, Token
- Multi-store secret fallback hierarchy
- Pydantic and JSON Schema validation with defaults
- Type-safe configuration access with `Config[T]` generic
- Dynamic reloading with file watching and incremental updates
- Configuration versioning with save, rollback, and diff
- Configuration drift detection
- Deep merge with per-path merge strategies (REPLACE, MERGE, APPEND)
- Configuration composition with `_include` and `_defaults` directives
- Async/await API for non-blocking configuration loading
- Observability: metrics collection, event emission, access tracking
- Source tracking and introspection API (keys, has, get, schema, explain)
- Debug mode with source tracking and export
- IDE support with auto-generated type stubs
- ConfigBuilder fluent API
- CLI tools: validate, lint, export, debug, explain, diff, migrate, load
- Comprehensive example suite (11 self-contained examples)
- Sphinx documentation with API reference and user guides

[Unreleased]: https://github.com/confiify/confii-py/commits/main
