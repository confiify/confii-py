Overview
========

What is Confii?
---------------------

Confii is a modern, feature-rich configuration management library designed for Python applications.
It simplifies the complexity of managing application settings across different environments while providing
enterprise-grade capabilities for validation, security, and observability.

Why Confii?
-----------------

Traditional configuration management in Python often involves:
- Manual loading and merging from multiple sources
- String-key dictionaries with no IDE support (``config["database"]["host"]``)
- Custom validation logic scattered across the codebase
- No way to trace where a value came from
- No built-in secret management

Confii solves these problems. Load from any source, access as attributes:

.. code-block:: python

   config = Config(loaders=[YamlLoader("config.yaml")])
   config.database.host    # "db.example.com"
   config.database.port    # 5432
   config.app.debug        # False

Key capabilities:

* **Attribute-Style Access** - ``config.database.host`` instead of ``config["database"]["host"]``
* **Type Safety** - ``Config[T]`` with Pydantic models gives full IDE autocomplete
* **Secret Management** - ``${secret:key}`` resolved from AWS, Vault, Azure, GCP
* **Source Tracking** - Know exactly where every value came from
* **Developer Experience** - IDE autocomplete, debugging tools, introspection API
* **Production Ready** - Observability, versioning, drift detection
* **Async Support** - First-class async/await API

Use Cases
---------

Confii is ideal for:

* **Web Applications** - Manage environment-specific configurations
* **Microservices** - Centralized configuration with multiple sources
* **Cloud Applications** - Integration with AWS, Azure, GCP secret stores
* **Enterprise Applications** - Complex configurations with validation
* **DevOps Tools** - Configuration management for infrastructure code
* **CLI Tools** - Simple yet powerful configuration loading

Key Concepts
------------

**Configuration Sources**
   Load from files, environment variables, cloud storage, or custom loaders.

**Environment-Specific Configs**
   Manage different configurations for development, staging, and production.

**Schema Validation**
   Validate configurations against Pydantic models or JSON Schema.

**Secret Resolution**
   Automatically resolve secrets from external stores using placeholders.

**Dynamic Reloading**
   Automatically reload configurations when files change.

**Configuration Composition**
   Include and merge configurations from multiple files.

**Observability**
   Track configuration access patterns and changes with metrics.

For more details, see the :doc:`user_guide/index` section.
