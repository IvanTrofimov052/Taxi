import asyncio
import websockets

async def hello(n):
    uri = "ws://localhost:13765"
    async with websockets.connect(uri) as websocket:
        await websocket.send(n)
        greeting = await websocket.recv()
        print("> {}".format(greeting))


async def echo(websocket, path):
    async for message in websocket:
        return message

while True:
    n = input()
    asyncio.get_event_loop().run_until_complete(hello(n))
