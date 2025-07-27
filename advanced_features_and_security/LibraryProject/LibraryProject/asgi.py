"""
ASGI config for LibraryProject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD

https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/

=======
>>>>>>> f01b2bdd036a8086bdc21d1a132670d3bf93d9ef
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

application = get_asgi_application()
