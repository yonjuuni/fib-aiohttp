import sys

from aiohttp import web
from api import create_app


app = create_app()


def runserver():
    web.run_app(app)

if 'runserver' in sys.argv:
    runserver()
