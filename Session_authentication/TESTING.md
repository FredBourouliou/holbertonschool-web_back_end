# Testing Guide for Basic Authentication API

## Prerequisites

Install the required packages:
```bash
pip3 install --break-system-packages -r requirements.txt
```

## Unit Tests

### Test 1: Auth Class Basic Functionality (Task 3)
```bash
python3 main_0.py
```
Expected output:
```
False
None
None
```

### Test 2: require_auth Method (Task 4)
```bash
python3 main_1.py
```
Expected output:
```
True
True
True
False
False
True
True
```

### Test 3: Extract Base64 Authorization Header (Task 7)
```bash
python3 main_2.py
```
Expected output:
```
None
None
None
Holberton
SG9sYmVydG9u
SG9sYmVydG9uIFNjaG9vbA==
None
```

### Test 4: Decode Base64 Authorization Header (Task 8)
```bash
python3 main_3.py
```
Expected output:
```
None
None
None
Holberton
Holberton School
Holberton School
```

## Integration Tests with API

### Start the API Server (Terminal 1)

Without authentication:
```bash
API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```

With basic authentication:
```bash
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
```

### Test API Endpoints (Terminal 2)

#### Test 1: Status Endpoint (No Auth Required)
```bash
curl "http://0.0.0.0:5000/api/v1/status"
```
Expected: `{"status":"OK"}`

#### Test 2: Unauthorized Endpoint (Task 1)
```bash
curl "http://0.0.0.0:5000/api/v1/unauthorized"
```
Expected: `{"error":"Unauthorized"}` with HTTP 401

#### Test 3: Forbidden Endpoint (Task 2)
```bash
curl "http://0.0.0.0:5000/api/v1/forbidden"
```
Expected: `{"error":"Forbidden"}` with HTTP 403

#### Test 4: Protected Endpoint Without Auth (Task 5)
```bash
curl "http://0.0.0.0:5000/api/v1/users"
```
Expected: `{"error":"Unauthorized"}` with HTTP 401

#### Test 5: Protected Endpoint With Invalid Auth
```bash
curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
```
Expected: `{"error":"Forbidden"}` with HTTP 403

#### Test 6: Create a Test User
Create a test script to add a user:
```python
#!/usr/bin/env python3
import base64
from models.user import User

user = User()
user.email = "bob@hbtn.io"
user.password = "H0lbertonSchool98!"
user.save()

basic_clear = "{}:{}".format(user.email, "H0lbertonSchool98!")
print("User created: {}".format(user.id))
print("Basic Base64: {}".format(base64.b64encode(basic_clear.encode('utf-8')).decode("utf-8")))
```

#### Test 7: Access Protected Endpoint With Valid Auth (Task 11)
```bash
curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
```
Expected: JSON array of users

#### Test 8: Test Password With Colon (Task 12)
Create a user with password containing `:`:
```python
user = User()
user.email = "test@example.com"
user.password = "Pass:word:123"
user.save()
# Then test with appropriate Base64 encoded credentials
```

#### Test 9: Test Wildcard Paths (Task 13)
The `require_auth` method supports wildcards:
```python
from api.v1.auth.auth import Auth
a = Auth()
print(a.require_auth("/api/v1/status", ["/api/v1/stat*"]))  # False
print(a.require_auth("/api/v1/stats", ["/api/v1/stat*"]))   # False
print(a.require_auth("/api/v1/users", ["/api/v1/stat*"]))   # True
```

## Code Style Check

Run pycodestyle on all Python files:
```bash
pycodestyle api/ models/
```

## Documentation Check

Check module documentation:
```bash
python3 -c 'print(__import__("api.v1.auth.auth").__doc__)'
```

Check class documentation:
```bash
python3 -c 'print(__import__("api.v1.auth.auth").v1.auth.auth.Auth.__doc__)'
```

Check method documentation:
```bash
python3 -c 'print(__import__("api.v1.auth.auth").v1.auth.auth.Auth.require_auth.__doc__)'
```

## Summary of Implemented Features

- [x] Task 0: Simple Basic API setup
- [x] Task 1: 401 Unauthorized error handler
- [x] Task 2: 403 Forbidden error handler
- [x] Task 3: Auth class with basic methods
- [x] Task 4: require_auth method with path checking
- [x] Task 5: Request validation with before_request
- [x] Task 6: BasicAuth class
- [x] Task 7: Extract Base64 from Authorization header
- [x] Task 8: Decode Base64 authorization header
- [x] Task 9: Extract user credentials from Base64
- [x] Task 10: Get User object from credentials
- [x] Task 11: Override current_user in BasicAuth
- [x] Task 12: Allow passwords with ":"
- [x] Task 13: Support wildcards in excluded_paths
