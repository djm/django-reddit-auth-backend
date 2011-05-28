from Cookie import SimpleCookie

import requests
from django.contrib.auth.models import User

from reddit_auth.settings import LOGIN_URL


class RedditBackend(object):
    """
    A custom authentication backend for Django which provided
    with a username and password utilises the Reddit Auth API
    to check if a user is authorised to login.
    """

    supports_object_permissions = False
    supports_anonymous_user = False
    supports_inactive_user = False

    def authenticate(self, username=None, password=None):
        """
        Given a reddit username and password, authenticates
        against the Reddit auth API and returns a relevant
        django.contrib.auth.models.User.
        """
        reddit_user = RedditUser(username, password)
        if reddit_user.is_authenticated():
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = User(username=username)
                # Explicit is better than implicit..
                user.is_staff = False
                user.is_superuser = False
                user.set_unusable_password
                user.save()                
            return user
        return None


class RedditUser(object):
    """
    A class to mimic a Reddit user in its most simplest form.
    """

    username = None
    password = None
    is_authenticated = False
    session_key = None

    def __init__(self, reddit_username, reddit_password):
        self.username = reddit_username
        self.password = reddit_password

    def is_authenticated(self):
        if self.username and self.password:
            post_data = {
                    'user': self.username,
                    'passwd': self.password
                   }
            response = requests.post(LOGIN_URL, data=post_data)
            cookie = SimpleCookie()
            cookie.load(response.headers.get('set-cookie'))
            # The API docs state that is the cookie returned
            # contains a reddit_session key only if the auth
            # was succesful. Unsuccesful responses will still
            # return a cookie, but with a 'reddit_first' key.
            if cookie.has_key('reddit_session'):
                self.session_key = cookie['reddit_session']
                return True
        return None
