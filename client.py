import websockets
import asyncio


async def listen():

    url = "wss://websocket-server1.glitch.me/"

    async with websockets.connect(url) as ws:
        while True:
            msg = await ws.recv()
            print(msg)

asyncio.get_event_loop().run_until_complete(listen())