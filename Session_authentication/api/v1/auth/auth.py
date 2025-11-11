#!/usr/bin/env python3
"""
Auth module for the API
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """
    Auth class to manage API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path
        Args:
            path: the path to check
            excluded_paths: list of paths that don't require authentication
        Returns:
            True if path requires authentication, False otherwise
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Normalize path to ensure it ends with /
        normalized_path = path if path.endswith('/') else path + '/'

        for excluded_path in excluded_paths:
            # Handle wildcard patterns (Task 13)
            if excluded_path.endswith('*'):
                # Remove the * and check if path starts with the prefix
                prefix = excluded_path[:-1]
                if (normalized_path.startswith(prefix) or
                        path.startswith(prefix)):
                    return False
            else:
                # Normalize excluded_path to ensure it ends with /
                normalized_excluded = (excluded_path if
                                       excluded_path.endswith('/') else
                                       excluded_path + '/')
                if normalized_path == normalized_excluded:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Gets the authorization header from the request
        Args:
            request: Flask request object
        Returns:
            The value of the Authorization header or None
        """
        if request is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Gets the current user from the request
        Args:
            request: Flask request object
        Returns:
            None (will be implemented in subclasses)
        """
        return None

    def session_cookie(self, request=None):
        """
        Returns a cookie value from a request
        Args:
            request: Flask request object
        Returns:
            The value of the session cookie or None
        """
        if request is None:
            return None

        # Get the cookie name from environment variable SESSION_NAME
        session_name = getenv('SESSION_NAME')

        # Return the value of the cookie
        return request.cookies.get(session_name)
