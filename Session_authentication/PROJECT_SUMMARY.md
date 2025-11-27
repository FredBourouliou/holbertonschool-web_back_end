# Basic Authentication - Project Summary

## Project Overview

This project implements a complete Basic Authentication system for a Flask API, demonstrating the fundamental concepts of authentication, Base64 encoding, and authorization headers.

## Completed Tasks

### Task 0: Simple Basic API
- Created complete API structure with User model
- Implemented file-based serialization/deserialization
- Set up Flask application with CORS

### Task 1: 401 Unauthorized Error Handler
- Added error handler for 401 status code
- Created test endpoint `/api/v1/unauthorized`
- Returns JSON: `{"error": "Unauthorized"}`

### Task 2: 403 Forbidden Error Handler
- Added error handler for 403 status code
- Created test endpoint `/api/v1/forbidden`
- Returns JSON: `{"error": "Forbidden"}`

### Task 3: Auth Class
- Created `Auth` base class in `api/v1/auth/auth.py`
- Implemented three methods:
  - `require_auth(path, excluded_paths)` - Returns False
  - `authorization_header(request)` - Returns None
  - `current_user(request)` - Returns None

### Task 4: Define Routes Without Authentication
- Implemented `require_auth` method with path checking logic
- Slash-tolerant: `/api/v1/status` and `/api/v1/status/` treated equally
- Returns True if path requires auth, False if in excluded_paths

### Task 5: Request Validation
- Implemented `authorization_header` method to extract Authorization header
- Added `before_request` hook to validate all requests
- Checks authentication requirements and raises appropriate errors

### Task 6: BasicAuth Class
- Created `BasicAuth` class inheriting from `Auth`
- Set up conditional loading based on `AUTH_TYPE` environment variable
- Supports both `auth` and `basic_auth` types

### Task 7: Extract Base64 from Authorization Header
- Implemented `extract_base64_authorization_header` method
- Validates header format starts with "Basic "
- Returns the Base64 part after "Basic "

### Task 8: Decode Base64 Authorization Header
- Implemented `decode_base64_authorization_header` method
- Decodes Base64 string to UTF-8
- Handles invalid Base64 gracefully with try/except

### Task 9: Extract User Credentials
- Implemented `extract_user_credentials` method
- Splits decoded header on first `:` only (supports passwords with colons)
- Returns tuple of (email, password)

### Task 10: Get User Object from Credentials
- Implemented `user_object_from_credentials` method
- Searches database for user by email
- Validates password using `is_valid_password` method
- Returns User instance or None

### Task 11: Complete Basic Authentication
- Implemented `current_user` method in BasicAuth
- Chains all authentication methods together
- Provides complete request-to-user authentication flow

### Task 12 (Advanced): Allow Passwords with Colon
- Modified `extract_user_credentials` to split only on first `:`
- Supports passwords like "H0lberton:School:98!"
- Uses `index()` method to find first colon position

### Task 13 (Advanced): Wildcard Support in Excluded Paths
- Enhanced `require_auth` to support `*` wildcard
- Pattern `/api/v1/stat*` matches `/api/v1/status`, `/api/v1/stats`, etc.
- Maintains backward compatibility with exact path matching

## Project Structure

```
Basic_authentication/
├── api/
│   └── v1/
│       ├── app.py              # Main Flask app with error handlers
│       ├── auth/
│       │   ├── auth.py         # Base Auth class
│       │   └── basic_auth.py   # BasicAuth implementation
│       └── views/
│           ├── index.py        # Status and test endpoints
│           └── users.py        # User CRUD operations
├── models/
│   ├── base.py                 # Base model with serialization
│   └── user.py                 # User model with password hashing
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── TESTING.md                  # Testing guide
└── PROJECT_SUMMARY.md          # This file
```

## Key Features

1. **Complete Authentication System**
   - Base Auth class for extensibility
   - BasicAuth implementation with Base64 encoding
   - Request validation with before_request hook

2. **Security Features**
   - Password hashing with SHA256
   - Base64 encoding for credentials
   - Proper error handling (401/403)

3. **Code Quality**
   - Follows pycodestyle (PEP 8)
   - Comprehensive documentation for all modules, classes, and methods
   - Type hints for better code clarity

4. **Advanced Features**
   - Support for passwords containing colons
   - Wildcard pattern matching in excluded paths
   - Slash-tolerant path matching

## Testing

All functionality has been tested:
- Unit tests for Auth and BasicAuth classes
- Integration tests with Flask API
- Wildcard pattern matching tests
- Password with colon tests
- All tests passing ✓

## Usage

Start the API with Basic Authentication:
```bash
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
```

Access protected endpoint:
```bash
# Without auth - returns 401
curl "http://0.0.0.0:5000/api/v1/users"

# With valid auth - returns user list
curl "http://0.0.0.0:5000/api/v1/users" \
  -H "Authorization: Basic <base64_credentials>"
```

## Learning Outcomes

Through this project, I learned:
- How authentication systems work
- Base64 encoding and decoding
- HTTP Authorization header usage
- Flask before_request hooks
- Error handling in web APIs
- Test-driven development
- Code quality standards (pycodestyle)

## Author

Holberton School Project - Basic Authentication Module
