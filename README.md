
#django-reddit-auth-backend (SERIOUS ALPHA - TESTS/MORE WORK ON THEIR WAY)

**A pluggable authencation backend for Django which allows authentication via the
Reddit API with a valid reddit username and password. Please read the NB below.**

##Install

Till this is ready for PyPi, install is from github.

If you're using pip:


    pip install -e git+https://TODO

Otherwise, simply clone or export from the git repo URL and run `python
setup.py install`.

##Setup

You will need to add to or replace the default AUTHENTICATION_BACKENDS setting
in your project's `settings.py`.

The authentication backends are used in the order they are defined and thus
thus multiple ones can be used; Django will simply try and authentice against
each one in turn until a valid user is returned.

I would recommend leaving in the default Django Auth model backend so as not to
lose access to groups, superuser & permissions etc.

e.g


    AUTHENTICATION_BACKENDS = (
        'reddit_auth.backends.RedditBackend',
        'django.contrib.auth.backends.ModelBackend',
    )


**NB**: reddit's API uptime is currently not great so beware that utilising this
backend as your *sole* authentication backend is unadvisable unless you want to
share their level of uptime.

##Use

Simply set up login as per usual but utilise your reddit username and password
to authenticate; if a succesful authentication is occuring for the first
time, this backend will create the necessary Django auth model with the same
username as the reddit account and therefore linked 1-to-1.

##License & Contributing

Licensed for use under the BSD v2 license.

To contribute, either submit a ticket in the github issue tracker or simply
fork the project and submit a pull request.
