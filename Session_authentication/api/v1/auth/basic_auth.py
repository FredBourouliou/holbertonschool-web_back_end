#!/usr/bin/env python3
"""
BasicAuth module for the API
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """
    BasicAuth class that inherits from Auth
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header
        for Basic Authentication
        Args:
            authorization_header: the Authorization header string
        Returns:
            The Base64 part of the header or None
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decodes the Base64 authorization header
        Args:
            base64_authorization_header: the Base64 string to decode
        Returns:
            The decoded value as UTF8 string or None
        """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extracts user email and password from the Base64 decoded value
        Args:
            decoded_base64_authorization_header: decoded Base64 string
        Returns:
            Tuple of (email, password) or (None, None)
        """
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        # Task 12: Allow passwords with ":" by splitting only on the first ":"
        split_index = decoded_base64_authorization_header.index(':')
        email = decoded_base64_authorization_header[:split_index]
        password = decoded_base64_authorization_header[split_index + 1:]

        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Returns the User instance based on email and password
        Args:
            user_email: user's email
            user_pwd: user's password
        Returns:
            User instance or None
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({'email': user_email})
        except Exception:
            return None

        if not users or len(users) == 0:
            return None

        user = users[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the User instance for a request
        Args:
            request: Flask request object
        Returns:
            User instance or None
        """
        auth_header = self.authorization_header(request)

        if auth_header is None:
            return None

        base64_header = self.extract_base64_authorization_header(auth_header)

        if base64_header is None:
            return None

        decoded_header = self.decode_base64_authorization_header(base64_header)

        if decoded_header is None:
            return None

        email, password = self.extract_user_credentials(decoded_header)

        if email is None or password is None:
            return None

        user = self.user_object_from_credentials(email, password)

        return user
