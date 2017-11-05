from aiohttp import web

from app.application import app

if __name__ == '__main__':
    web.run_app(app, port=8000)