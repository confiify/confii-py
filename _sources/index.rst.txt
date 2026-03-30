Confii
======

.. image:: _static/confii-py.png
   :align: center
   :alt: Confii

**A comprehensive, production-ready configuration management library for Python.**

.. image:: https://img.shields.io/pypi/v/confii
   :target: https://pypi.org/project/confii/
   :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/confii
   :target: https://pypi.org/project/confii/
   :alt: Python Versions

.. image:: https://img.shields.io/github/license/confiify/confii-py
   :target: https://github.com/confiify/confii-py/blob/main/LICENSE.txt
   :alt: License

.. image:: https://img.shields.io/github/actions/workflow/status/confiify/confii-py/ci.yml?branch=main
   :target: https://github.com/confiify/confii-py/actions
   :alt: CI Status

----

Confii provides a unified interface for loading, merging, validating, and accessing
configuration from multiple sources with enterprise-grade features like secret management,
schema validation, observability, versioning, and async support.

Getting Started
---------------

Install Confii:

.. code-block:: bash

   pip install confii

Load your first config:

.. code-block:: python

   from confii import Config
   from confii.loaders import YamlLoader

   config = Config(loaders=[YamlLoader("config.yaml")])
   print(config.database.host)

Key Features
------------

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - **Configuration Sources**
     - YAML, JSON, TOML, INI, .env, environment variables, AWS S3, Azure Blob, GCS, HTTP, Git
   * - **Secret Management**
     - AWS Secrets Manager, HashiCorp Vault (9 auth methods), Azure Key Vault, GCP Secret Manager
   * - **Type Safety**
     - ``Config[T]`` generics with Pydantic models, full IDE autocomplete
   * - **Validation**
     - Pydantic and JSON Schema validation with defaults
   * - **Dynamic Reloading**
     - File watching with incremental reload, on-change callbacks
   * - **Merge Strategies**
     - 6 strategies (replace, merge, append, prepend, intersection, union) with per-path overrides
   * - **Introspection**
     - ``keys()``, ``has()``, ``get()``, ``explain()``, ``schema()``, source tracking
   * - **Versioning**
     - Save, compare, and rollback configuration versions
   * - **Drift Detection**
     - Compare actual vs intended configuration
   * - **Observability**
     - Access metrics, event emission, debug reports
   * - **Async Support**
     - First-class async/await API
   * - **CLI Tools**
     - validate, export, debug, explain, diff, migrate, lint, load

Documentation
-------------

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   overview
   installation
   quickstart
   user_guide/index

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   api/index

.. toctree::
   :maxdepth: 1
   :caption: Resources

   examples
   contributing

Links
-----

* **Source Code**: `GitHub <https://github.com/confiify/confii-py>`_
* **Package**: `PyPI <https://pypi.org/project/confii/>`_
* **Issues**: `Bug Tracker <https://github.com/confiify/confii-py/issues>`_

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
