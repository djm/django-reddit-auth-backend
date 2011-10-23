from django.conf import settings

DEFAULT_LOGIN_URL = 'http://www.reddit.com/api/login'

LOGIN_URL = getattr(settings, 'REDDIT_AUTH_LOGIN_URL', DEFAULT_LOGIN_URL)
