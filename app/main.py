from aiohttp import web

from routes import setup_routes

app = web.Application()


if __name__ == '__main__':
    setup_routes(app)
    web.run_app(app, host='0.0.0.0', port=8080)

