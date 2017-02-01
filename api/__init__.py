import pathlib
import yaml
from aiohttp import web
from aiocache import SimpleMemoryCache

cache = SimpleMemoryCache(timeout=60)


def create_app(config='default'):

    from api.v1 import v1

    conf = yaml.load(open(str(pathlib.Path('.') / 'config.yml'), 'r'))

    app = web.Application(debug=conf['debug'][config])
    app.router.add_subapp('/v1/', v1)

    app['config'] = conf

    return app
