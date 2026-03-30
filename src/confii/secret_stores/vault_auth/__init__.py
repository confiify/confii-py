"""Vault authentication methods for HashiCorp Vault integration.

This module provides various authentication methods for HashiCorp Vault,
supporting enterprise scenarios including OIDC, Kerberos, LDAP, Kubernetes, etc.

Example:
    >>> from confii.secret_stores.vault_auth import OIDCAuth, KerberosAuth
    >>> from confii.secret_stores import HashiCorpVault
    >>>
    >>> # OIDC with Kerberos
    >>> auth = OIDCAuth(role="myapp-role", use_kerberos=True)
    >>> vault = HashiCorpVault(url="https://vault.example.com", auth_method=auth)
    >>>
    >>> # Or LDAP
    >>> auth = LDAPAuth(username="user", password="pass")
    >>> vault = HashiCorpVault(url="https://vault.example.com", auth_method=auth)
"""

from confii.secret_stores.vault_auth.approle import AppRoleAuth
from confii.secret_stores.vault_auth.aws import AWSAuth
from confii.secret_stores.vault_auth.azure import AzureAuth
from confii.secret_stores.vault_auth.base import VaultAuthMethod
from confii.secret_stores.vault_auth.gcp import GCPAuth
from confii.secret_stores.vault_auth.jwt import JWTAuth
from confii.secret_stores.vault_auth.kubernetes import KubernetesAuth
from confii.secret_stores.vault_auth.ldap import LDAPAuth
from confii.secret_stores.vault_auth.oidc import OIDCAuth
from confii.secret_stores.vault_auth.token import TokenAuth

__all__ = [
    "AWSAuth",
    "AppRoleAuth",
    "AzureAuth",
    "GCPAuth",
    "JWTAuth",
    "KubernetesAuth",
    "LDAPAuth",
    "OIDCAuth",
    "TokenAuth",
    "VaultAuthMethod",
]
