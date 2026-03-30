Quick Start
===========

This guide will help you get started with Confii in minutes.

Basic Usage
-----------

Load configuration from a file and access values as attributes:

.. code-block:: python

   from confii import Config
   from confii.loaders import YamlLoader

   config = Config(loaders=[YamlLoader("config.yaml")])

   # Access values directly as nested attributes
   print(config.database.host)       # "localhost"
   print(config.database.port)       # 5432
   print(config.app.debug)           # False
   print(config.app.name)            # "MyApp"

That's it — no ``.get()`` calls, no string keys, no brackets.

Multiple Sources
----------------

Load from multiple sources (later sources override earlier ones):

.. code-block:: python

   from confii import Config
   from confii.loaders import YamlLoader, EnvironmentLoader

   config = Config(
       env="production",
       loaders=[
           YamlLoader("config/base.yaml"),
           YamlLoader("config/production.yaml"),
           EnvironmentLoader("APP"),  # APP_DATABASE__HOST -> database.host
       ]
   )

   # Values are merged — access the result directly
   print(config.database.host)       # from production.yaml
   print(config.database.port)       # from base.yaml (not overridden)
   print(config.cache.ttl)           # from base.yaml

With Secret Stores
------------------

Use secret stores for secure credential management:

.. code-block:: python

   from confii import Config
   from confii.secret_stores import AWSSecretsManager, SecretResolver
   from confii.loaders import YamlLoader

   secret_store = AWSSecretsManager(region_name='us-east-1')
   config = Config(
       loaders=[YamlLoader("config.yaml")],
       secret_resolver=SecretResolver(secret_store)
   )

   # Secrets are resolved transparently — access like any other value
   print(config.database.password)   # resolved from AWS Secrets Manager
   print(config.api.key)             # resolved from "${secret:api/key}"

With Schema Validation
----------------------

Validate configurations with Pydantic models:

.. code-block:: python

   from confii import Config
   from confii.loaders import YamlLoader
   from pydantic import BaseModel

   class DatabaseConfig(BaseModel):
       host: str
       port: int = 5432

   config = Config(
       loaders=[YamlLoader("config.yaml")],
       schema=DatabaseConfig,
       validate_on_load=True
   )

   # Validated — attribute access is guaranteed to match the schema
   print(config.database.host)       # guaranteed str
   print(config.database.port)       # guaranteed int

For full type safety with IDE autocomplete, use ``Config[T]``:

.. code-block:: python

   config = Config[AppConfig](
       loaders=[YamlLoader("config.yaml")],
       schema=AppConfig,
       validate_on_load=True,
   )

   config.typed.database.host   # IDE knows: str
   config.typed.database.port   # IDE knows: int

Debug Mode
----------

Enable debug mode to trace where each value came from:

.. code-block:: python

   config = Config(debug_mode=True, loaders=[YamlLoader("config.yaml")])

   # Use config normally
   print(config.database.host)

   # Trace the source
   info = config.get_source_info("database.host")
   print(f"From: {info.source_file}")  # "config.yaml"

Alternative Access Methods
--------------------------

While attribute access is the primary way to use Confii, other methods are available:

.. code-block:: python

   # get() — useful when you need defaults or have dynamic keys
   config.get("database.host", "localhost")

   # has() — check if a key exists
   config.has("database.ssl")

   # keys() — list all keys
   config.keys()
   config.keys("database")   # keys under a prefix

   # explain() — full resolution details
   config.explain("database.host")

Next Steps
----------

* See the :doc:`user_guide/index` for detailed usage
* Check out the :doc:`api/index` for complete API reference
* Browse :doc:`examples` for more examples
