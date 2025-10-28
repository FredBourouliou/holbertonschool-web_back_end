#!/usr/bin/env python3
"""
Test password with colon (Task 12)
"""
from api.v1.auth.basic_auth import BasicAuth

a = BasicAuth()

# Test extracting credentials with password containing colons
print("Testing password with colons:")
print()

# Test 1: Simple password
result = a.extract_user_credentials("user@example.com:password123")
print(f"Input: 'user@example.com:password123'")
print(f"Result: {result}")
print(f"Expected: ('user@example.com', 'password123')")
print()

# Test 2: Password with one colon
result = a.extract_user_credentials("user@example.com:pass:word")
print(f"Input: 'user@example.com:pass:word'")
print(f"Result: {result}")
print(f"Expected: ('user@example.com', 'pass:word')")
print()

# Test 3: Password with multiple colons
result = a.extract_user_credentials("user@example.com:H0lberton:School:98!")
print(f"Input: 'user@example.com:H0lberton:School:98!'")
print(f"Result: {result}")
print(f"Expected: ('user@example.com', 'H0lberton:School:98!')")
print()

# Test 4: Email with subdomain and complex password
result = a.extract_user_credentials("admin@sub.example.com:p@ss:w0rd:123:!")
print(f"Input: 'admin@sub.example.com:p@ss:w0rd:123:!'")
print(f"Result: {result}")
print(f"Expected: ('admin@sub.example.com', 'p@ss:w0rd:123:!')")
