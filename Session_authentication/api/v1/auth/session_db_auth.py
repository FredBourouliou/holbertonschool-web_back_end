#!/usr/bin/env python3
"""
SessionDBAuth module for the API with database storage
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """
    SessionDBAuth class to manage API session authentication with database
    """

    def create_session(self, user_id=None):
        """
        Create and store new instance of UserSession and return Session ID
        Args:
            user_id: the user ID to create a session for
        Returns:
            The Session ID or None
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        # Create and save UserSession instance
        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Returns the User ID by requesting UserSession in database
        Args:
            session_id: the Session ID to look up
        Returns:
            The User ID or None
        """
        if session_id is None:
            return None

        # Search for UserSession in database
        user_sessions = UserSession.search({'session_id': session_id})

        if not user_sessions or len(user_sessions) == 0:
            return None

        user_session = user_sessions[0]

        # Check if session has expired (using parent method logic)
        if self.session_duration <= 0:
            return user_session.user_id

        # Check if session has expired based on created_at
        from datetime import datetime, timedelta

        created_at = user_session.created_at
        if created_at is None:
            return None

        expiration_time = created_at + timedelta(seconds=self.session_duration)
        if expiration_time < datetime.utcnow():
            return None

        return user_session.user_id

    def destroy_session(self, request=None):
        """
        Destroys the UserSession based on Session ID from request cookie
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

        # Search for UserSession in database
        user_sessions = UserSession.search({'session_id': session_id})

        if not user_sessions or len(user_sessions) == 0:
            return False

        user_session = user_sessions[0]

        # Remove the UserSession from database
        user_session.remove()

        return True
