"""
WSGI config for ezo2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os, sys
print("version python", sys.version)

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/ezo-chan/ezo2Project/ezo2')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ezo2.settings")

application = get_wsgi_application()
