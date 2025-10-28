# Quick Start Guide

## Installation

1. Install dependencies:
```bash
pip3 install --break-system-packages -r requirements.txt
```

## Running Tests

```bash
# Test basic Auth class functionality
python3 main_0.py

# Test require_auth with path checking
python3 main_1.py

# Test Base64 extraction
python3 main_2.py

# Test Base64 decoding
python3 main_3.py

# Test wildcard patterns (Task 13)
python3 test_wildcard.py

# Test passwords with colons (Task 12)
python3 test_password_colon.py
```

## Running the API

### Without Authentication
```bash
API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```

### With Basic Authentication
```bash
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
```

## Testing the API

In a separate terminal:

```bash
# Check status (no auth required)
curl "http://0.0.0.0:5000/api/v1/status"

# Test 401 error
curl "http://0.0.0.0:5000/api/v1/unauthorized"

# Test 403 error
curl "http://0.0.0.0:5000/api/v1/forbidden"

# Access protected endpoint without auth (returns 401)
curl "http://0.0.0.0:5000/api/v1/users"

# Create a test user and get credentials
python3 << 'EOF'
import base64
from models.user import User

user = User()
user.email = "bob@hbtn.io"
user.password = "H0lbertonSchool98!"
user.save()

credentials = f"{user.email}:H0lbertonSchool98!"
encoded = base64.b64encode(credentials.encode()).decode()
print(f"User ID: {user.id}")
print(f"Encoded credentials: {encoded}")
EOF

# Access protected endpoint with auth
curl "http://0.0.0.0:5000/api/v1/users" \
  -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
```

## Code Quality Check

```bash
# Check code style
pycodestyle api/ models/

# Check documentation
python3 -c 'print(__import__("models.user").__doc__)'
python3 -c 'print(__import__("models.user").user.User.__doc__)'
```

## Project Structure

```
Basic_authentication/
├── api/v1/
│   ├── app.py           # Flask app
│   ├── auth/
│   │   ├── auth.py      # Base Auth class
│   │   └── basic_auth.py # BasicAuth implementation
│   └── views/
│       ├── index.py     # Test endpoints
│       └── users.py     # User endpoints
├── models/
│   ├── base.py          # Base model
│   └── user.py          # User model
└── requirements.txt     # Dependencies
```

## All Tasks Completed ✓

- [x] Task 0: Simple Basic API
- [x] Task 1: 401 Error Handler
- [x] Task 2: 403 Error Handler
- [x] Task 3: Auth Class
- [x] Task 4: require_auth Method
- [x] Task 5: Request Validation
- [x] Task 6: BasicAuth Class
- [x] Task 7: Extract Base64
- [x] Task 8: Decode Base64
- [x] Task 9: Extract Credentials
- [x] Task 10: User from Credentials
- [x] Task 11: current_user Override
- [x] Task 12: Passwords with ":"
- [x] Task 13: Wildcard Patterns

## Next Steps

For more details, see:
- `README.md` - Project overview
- `TESTING.md` - Comprehensive testing guide
- `PROJECT_SUMMARY.md` - Detailed implementation summary
