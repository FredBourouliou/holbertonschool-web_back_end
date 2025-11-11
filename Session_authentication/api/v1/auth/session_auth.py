#!/usr/bin/env python3
"""
SessionAuth module for the API
"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """
    SessionAuth class to manage API session authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session ID for a user_id
        Args:
            user_id: the user ID to create a session for
        Returns:
            The Session ID or None
        """
        if user_id is None:
            return None

        if not isinstance(user_id, str):
            return None

        # Generate a Session ID using uuid4()
        session_id = str(uuid.uuid4())

        # Store the user_id with session_id as key
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns a User ID based on a Session ID
        Args:
            session_id: the Session ID to look up
        Returns:
            The User ID or None
        """
        if session_id is None:
            return None

        if not isinstance(session_id, str):
            return None

        # Use .get() to retrieve the user_id from the dictionary
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Returns a User instance based on a cookie value
        Args:
            request: Flask request object
        Returns:
            User instance or None
        """
        # Get the session cookie value
        session_cookie = self.session_cookie(request)

        # Get the user ID from the session ID
        user_id = self.user_id_for_session_id(session_cookie)

        # Return the User instance
        return User.get(user_id)

    def destroy_session(self, request=None):
        """
        Deletes the user session / logout
        Args:
            request: Flask request object
        Returns:
            True if session was destroyed, False otherwise
        """
        if request is None:
            return False

        # Get the session cookie
        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        # Get the user ID for this session
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        # Delete the session ID from the dictionary
        del self.user_id_by_session_id[session_id]

        return True
