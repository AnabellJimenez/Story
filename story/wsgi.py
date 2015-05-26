"""
WSGI config for story project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application
from dj_static import Cling
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "story.settings")


application = Cling(get_wsgi_application())
application = DjangoWhiteNoise(application)

