import pytest
from aiohttp import web
from views import ip_scaner

@pytest.fixture
def cli(event_loop, aiohttp_client):
    app = web.Application()
    app.router.add_get('/scaner', ip_scaner)
    return event_loop.run_until_complete(aiohttp_client(app))


async def test_get_value(cli):
    resp = await cli.get(
        '/scaner',
        params={
            'begin': 8080,
            'end': 8080,
            'ip': 'steemit.com'
        }
    )
    assert resp.status == 200
    assert await resp.json() == [{"port": 8080, "status": "open"}]


async def test_get_empty(cli):
    resp = await cli.get('/scaner')
    assert resp.status == 200
    result = await resp.json()
    assert len(result) == 65536


async def test_wrong_request(cli):
    resp = await cli.get('/')
    assert resp.status == 404


async def test_wrong_ports(cli):
    resp = await cli.get(
        '/scaner',
        params={
            'begin': 8090,
            'end': 8080,
            'ip': 'steemit.com'
        }
    )
    assert resp.status == 200
    assert await resp.json() == []
