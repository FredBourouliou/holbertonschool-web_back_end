#!/usr/bin/env python3
"""
Test wildcard functionality (Task 13)
"""
from api.v1.auth.auth import Auth

a = Auth()

# Test wildcard patterns
print("Testing wildcard patterns:")
print("Path: /api/v1/status, Pattern: ['/api/v1/stat*']")
print("Result:", a.require_auth("/api/v1/status", ["/api/v1/stat*"]))
print("Expected: False")
print()

print("Path: /api/v1/stats, Pattern: ['/api/v1/stat*']")
print("Result:", a.require_auth("/api/v1/stats", ["/api/v1/stat*"]))
print("Expected: False")
print()

print("Path: /api/v1/users, Pattern: ['/api/v1/stat*']")
print("Result:", a.require_auth("/api/v1/users", ["/api/v1/stat*"]))
print("Expected: True")
print()

print("Path: /api/v1/status/, Pattern: ['/api/v1/stat*']")
print("Result:", a.require_auth("/api/v1/status/", ["/api/v1/stat*"]))
print("Expected: False")
