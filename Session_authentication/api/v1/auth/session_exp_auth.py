#!/usr/bin/env python3
"""
SessionExpAuth module for the API with session expiration
"""
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """
    SessionExpAuth class to manage API session authentication with expiration
    """

    def __init__(self):
        """
        Initialize SessionExpAuth instance
        """
        super().__init__()
        try:
            self.session_duration = int(getenv('SESSION_DURATION', 0))
        except ValueError:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """
        Create a Session ID for a user_id with expiration
        Args:
            user_id: the user ID to create a session for
        Returns:
            The Session ID or None
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        # Create session dictionary with user_id and created_at
        session_dict = {
            'user_id': user_id,
            'created_at': datetime.now()
        }

        # Store the session dictionary
        self.user_id_by_session_id[session_id] = session_dict

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Returns a User ID based on a Session ID with expiration check
        Args:
            session_id: the Session ID to look up
        Returns:
            The User ID or None
        """
        if session_id is None:
            return None

        # Get the session dictionary
        session_dict = self.user_id_by_session_id.get(session_id)
        if session_dict is None:
            return None

        # If session_duration is 0 or less, session never expires
        if self.session_duration <= 0:
            return session_dict.get('user_id')

        # Check if created_at exists in session dictionary
        created_at = session_dict.get('created_at')
        if created_at is None:
            return None

        # Check if session has expired
        expiration_time = created_at + timedelta(seconds=self.session_duration)
        if expiration_time < datetime.now():
            return None

        return session_dict.get('user_id')
