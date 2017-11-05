import base64
import logging

from aiohttp import web
import rapidjson as json

from .api import setup_sport_routes
from .models import setup_tables

async def request_logger(app, handler):
    logger = logging.getLogger('request_logger')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.FileHandler('request.log'))

    async def middleware(request):
        """Middleware to log requests."""
        resp = await handler(request)
        try:
            data = json.loads(await request.text())
            data = json.dumps(data, sort_keys=True)
        except Exception:
            data = base64.b64encode((await request.text()).encode('utf-8'))

        logger.debug('host:{host} ip:{ip} body:{body}'.format(
            host=request.host,
            ip=request.transport.get_extra_info('peername'),
            body=data,
        ))
        return resp
    return middleware




app = web.Application(
    middlewares=[request_logger]
)
setup_tables()
setup_sport_routes(app)