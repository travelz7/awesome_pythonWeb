import asyncio

from aiohttp import web
from pip._internal.utils import logging


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')

def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv = yield from loop.create__server(app.make_handler(),'127.0.0.1',9000)
    logging.info("server started at http://127.0.0.1:9000...")
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()