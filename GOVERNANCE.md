# Governance

This document describes the governance model for the Confii project.

## Project Maintainers

The project is maintained by the [confiify](https://github.com/confiify) organization. Maintainers are responsible for:

- Reviewing and merging pull requests
- Triaging issues and managing the backlog
- Making release decisions
- Ensuring code quality and security standards

## Decision Making

- **Minor changes** (bug fixes, small improvements): A single maintainer review and approval is sufficient.
- **Major changes** (new features, breaking changes, architecture decisions): Require discussion in a GitHub issue or pull request before implementation. Maintainer consensus is preferred.
- **Release decisions**: Made by maintainers based on the state of the main branch and the changelog.

## Contributing

Anyone can contribute to Confii. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Contributors who demonstrate sustained, high-quality contributions may be invited to become maintainers.

## Release Process

1. Changes are merged to `main` via pull requests.
2. All CI checks must pass before merging.
3. Releases are created by pushing a version tag (e.g., `v1.0.0`).
4. The release workflow automatically publishes to PyPI using trusted publishing (OIDC).
5. GitHub Releases are auto-generated with release notes.

## Security

Security vulnerabilities should be reported according to [SECURITY.md](SECURITY.md). Maintainers will respond within 48 hours.

## Communication

- **Issues**: [GitHub Issues](https://github.com/confiify/confii-py/issues) for bugs and feature requests.
- **Discussions**: [GitHub Discussions](https://github.com/confiify/confii-py/discussions) for questions and ideas.
- **Security**: Private reporting via [GitHub Security Advisories](https://github.com/confiify/confii-py/security/advisories).
