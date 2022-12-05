"""
WSGI config for ajoubot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os, sys

sys.path.append('/home/ubuntu/ajoubot')
#sys.path.append('/home/ubuntu/ajoubot/ajoubot')
sys.path.append('/home/ubuntu/myvenv/lib/python3.5/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ajoubot.settings")

application = get_wsgi_application()
