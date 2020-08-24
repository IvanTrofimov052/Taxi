import asyncio
import websockets
from math import sqrt

def midlealgebr(a):
    sum = 0
    for i in range(len(a)):
        sum += int(a[i])
    return sum/(len(a) + 1)

def midlegeometry(a):
    mult = 1
    for i in range(len(a)):
        mult *= int(a[i])
    print(1 /(len(a) + 1))
    return pow(mult, 1 /(len(a) + 1))

def sample_span(a):
    return int(max(a)) -  int(min(a))


def makerequest(list):
    return 'среднее арифмитическое - ', str(midlealgebr(list)),\
           ' среднее геометрическое - ', str(midlegeometry(list)),\
           ' размах выборки - ', str(sample_span(list))


async def echo(websocket, path):
    async for message in websocket:
        try:
            await websocket.send(makerequest(message.split()))
        except:
            pass

start_server = websockets.serve(echo, "localhost", 13765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
