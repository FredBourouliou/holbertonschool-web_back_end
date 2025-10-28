# Basic Authentication

This project implements a Basic Authentication system for a simple Flask API.

## Description

In this project, you will learn what the authentication process means and implement a Basic Authentication on a simple API. For learning purposes, we walk through each step of this mechanism to understand it by doing.

## Learning Objectives

- What authentication means
- What Base64 is
- How to encode a string in Base64
- What Basic authentication means
- How to send the Authorization header

## Requirements

- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- Code should use the pycodestyle style (version 2.5)
- All files must be executable
- All modules, classes, and functions must have documentation

## Installation

```bash
pip3 install -r requirements.txt
```

## Usage

### Start the server

```bash
API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```

### Start with authentication

```bash
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
```

## API Endpoints

- `GET /api/v1/status` - Check API status
- `GET /api/v1/unauthorized` - Test 401 error
- `GET /api/v1/forbidden` - Test 403 error
- `GET /api/v1/users` - Get all users (requires authentication)
- `GET /api/v1/users/<user_id>` - Get specific user (requires authentication)

## Testing

```bash
# Check status (no auth required)
curl "http://0.0.0.0:5000/api/v1/status"

# Access users without auth (will fail)
curl "http://0.0.0.0:5000/api/v1/users"

# Access users with Basic auth
curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
```

## Project Structure

```
Basic_authentication/
├── api/
│   ├── __init__.py
│   └── v1/
│       ├── __init__.py
│       ├── app.py
│       ├── auth/
│       │   ├── __init__.py
│       │   ├── auth.py
│       │   └── basic_auth.py
│       └── views/
│           ├── __init__.py
│           ├── index.py
│           └── users.py
├── models/
│   ├── __init__.py
│   ├── base.py
│   └── user.py
├── requirements.txt
└── README.md
```

## Author

Holberton School Project
