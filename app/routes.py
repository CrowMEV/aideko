from aiohttp import web

from views import ip_scaner



def setup_routes(app):
    app.add_routes(
        [
            web.get('/scaner', ip_scaner)
        ]
    )
