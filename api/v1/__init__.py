from aiohttp import web

from api.v1 import methods


def error_pages(overrides):
    async def middleware(app, handler):
        async def middleware_handler(request):
            try:
                response = await handler(request)
                override = overrides.get(response.status)
                if override is None:
                    return response
                else:
                    return await override(request, response)
            except web.HTTPException as ex:
                override = overrides.get(ex.status)
                if override is None:
                    raise
                else:
                    return await override(request, ex)
        return middleware_handler
    return middleware

error_middleware = error_pages({404: methods.page_not_found})

v1 = web.Application()

v1.middlewares.append(error_middleware)
v1.router.add_get('/fib/{number}', methods.fib)
