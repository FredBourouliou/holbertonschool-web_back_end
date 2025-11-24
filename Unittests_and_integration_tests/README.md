# Unittests and Integration Tests

This project focuses on unit testing and integration testing in Python using the `unittest` framework.

## Learning Objectives

- Understand the difference between unit and integration tests
- Learn common testing patterns such as mocking, parametrizations, and fixtures
- Practice writing tests for functions, classes, and HTTP calls
- Use `unittest.mock` to patch external dependencies
- Implement integration tests with fixtures

## Requirements

- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.9
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- Code should use pycodestyle style (version 2.5)
- All files must be executable
- All modules, classes, and functions should have documentation
- All functions and coroutines must be type-annotated

## Files

- `utils.py`: Generic utilities for GitHub org client
- `client.py`: GitHub org client implementation
- `fixtures.py`: Test fixtures for integration tests
- `test_utils.py`: Unit tests for utils module
- `test_client.py`: Unit and integration tests for GithubOrgClient

## Running Tests

Execute tests with:

```bash
$ python -m unittest path/to/test_file.py
```

Or run all tests:

```bash
$ python -m unittest discover
```

## Tasks

0. **Parameterize a unit test** - Test `access_nested_map` function
1. **Parameterize a unit test** - Test exception handling for `access_nested_map`
2. **Mock HTTP calls** - Test `get_json` function with mocked HTTP requests
3. **Parameterize and patch** - Test the `memoize` decorator
4. **Parameterize and patch as decorators** - Test `GithubOrgClient.org`
5. **Mocking a property** - Test `_public_repos_url` property
6. **More patching** - Test `public_repos` method
7. **Parameterize** - Test `has_license` static method
8. **Integration test: fixtures** - Set up integration tests with fixtures
9. **Integration tests** - Test `public_repos` with and without license filter
