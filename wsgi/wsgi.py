#!/usr/bin/env python

import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.openshift')
sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'food_step'))

application = get_wsgi_application()
