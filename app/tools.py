import asyncio


async def check_port(ip, port):
    conn = asyncio.open_connection(ip, port)
    try:
        reader, writer = await asyncio.wait_for(conn, timeout=1)
        return {'port': int(port), 'status': 'open'}
    except:
        return {'port': int(port), 'status': 'close'}
    finally:
        if 'writer' in locals():
            writer.close()


async def get_ports_info(ports, ip):
    tasks = [asyncio.create_task(check_port(ip, port)) for port in ports]
    for task in tasks:
        yield await task