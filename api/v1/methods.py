from aiohttp.web import json_response

from api import cache


async def calculate_fib(n):
    result = [0, 1]
    for i in range(2, n + 1):
        result.append(result[-1] + result[-2])
    return result


async def fib(request):

    try:
        number = int(request.match_info['number'])
    except ValueError:
        return json_response({'error': 'Not an integer.'})

    if number > 1000:
        return json_response({'error': 'Try a number less than 1000.'})
    result = await cache.get(number)

    if result is None:
        result = await calculate_fib(number)
        await cache.set(number, result)

    return json_response({'sequence': result})


async def page_not_found(request, response):
    return json_response({'error': 'Invalid API call.'})