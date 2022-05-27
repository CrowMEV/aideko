import syslog
import asyncio
from aiohttp import web
from more_itertools import chunked

from tools import get_ports_info


async def ip_scaner(request):
    print(request.text)
    syslog.syslog(syslog.LOG_INFO, f'request from {request.remote}')
    result = []
    try:
        ip = request.query.get('ip', '127.0.0.1')
        begin = int(request.query.get('begin', 0))
        end = int(request.query.get('end', 65535))
        for ports in chunked(range(begin, end+1), 10):
            async for port in get_ports_info(ports, ip):
                result.append(port)
    except ValueError as err:
        syslog.syslog(syslog.LOG_ERR, str(err))
    return web.json_response(result)













#