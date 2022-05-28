import syslog
import asyncio
from aiohttp import web
from more_itertools import chunked

from tools import get_ports_info


async def ip_scaner(request):
    syslog.syslog(syslog.LOG_INFO, f'request from {request.remote}')
    result = []
    ip = request.query.get('ip', '127.0.0.1')
    begin = int(request.query.get('begin', 0))
    end = int(request.query.get('end', 65535))
    status = request.query.get('status')
    try:
        for ports in chunked(range(begin, end+1), 10):
            async for port in get_ports_info(ports, ip):
                result.append(port)
    except ValueError as err:
        syslog.syslog(syslog.LOG_ERR, str(err))
    if status:
        result = [port for port in result if port['status'] == status]
    return web.json_response(result)













#