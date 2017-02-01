import sys

from aiohttp import web
from api import create_app


app = create_app(config='default')


if 'runserver' in sys.argv:
    web.run_app(app)
else:
    print('\nInvalid arguments.\nUsage: python3 manage.py runserver')
