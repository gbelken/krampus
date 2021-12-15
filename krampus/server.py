import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import asyncio
import constants
from aiohttp import web
from ChristmasTree import ChristmasTree

hostName = "localhost"
serverPort = 80

ct = ChristmasTree() #Using Defaults
count = 0

effectSequence = [
    { 'id': 0, 'iteratorFunc': None,            'colorFunc': 'colorAlternator', 'effects': ['TopToBottom'], 'colors': [constants.RED, constants.GREEN] },
    { 'id': 1, 'iteratorFunc': None,            'colorFunc': 'colorAlternator', 'effects': ['TopToBottom'], 'colors': [constants.GREEN, constants.RED] },
    { 'id': 2, 'iteratorFunc': None,            'colorFunc': 'colorAlternator', 'effects': ['TopToBottom'], 'colors': [ constants.CLEAR ] },
    { 'id': 3, 'iteratorFunc': 'colorIterator', 'colorFunc': 'colorAlternator', 'effects': ['TreeSpiral'], 'colors': constants.rainbowColors },
    { 'id': 4, 'iteratorFunc': None,            'colorFunc': 'colorAlternator', 'effects': ['SnakeTheTree', 'TreeSpiral', 'RainbowTree', 'SegmentRotator', 'TopToBottom'], 'colors': constants.christmasColorsTraditional },
    { 'id': 5, 'iteratorFunc': 'colorIterator', 'colorFunc': 'randomColor', 'effects': ['TreeColor'], 'colors': constants.christmasColorsExtended },
    { 'id': 6, 'iteratorFunc': None,            'colorFunc': 'colorAlternator', 'effects': ['SnakeTheTree', 'TreeSpiral', 'RainbowTree', 'SegmentRotator', 'TopToBottom'], 'colors': constants.christmasColorsTraditional },
    { 'id': 7, 'iteratorFunc': None,            'colorFunc': 'colorAlternator', 'effects': ['RainbowTree'], 'colors': constants.rainbowColors },
    { 'id': 8, 'iteratorFunc': None,            'colorFunc': 'colorAlternator', 'effects': ['TreeSpiral'], 'colors': [ constants.CLEAR ] },
]

currentSequence = ""

async def effectWorker():
    global count
    global currentSequence
    
    await ct.sequenceRunner(effectSequence)

loop = asyncio.get_event_loop()

async def __initEffectLoop():
    try:
        asyncio.ensure_future(effectWorker())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing Loop")
        loop.close()

app = web.Application()
routes = web.RouteTableDef()

### API Routes ###########
@routes.get('/api/status')
async def get_status_handler(request):
    data = { "isLooping": False, 
            "Count": count, 
            "SequenceLoop": effectSequence, 
            "CurrentSequence": currentSequence }
    return web.json_response(data)

@routes.get('/api/start')
async def get_start_handler(request):
    await ct.StartAnimation()
    await ct.TreeColor(ct.getColor(constants.GREEN), [])
    return web.json_response({"Status": "On", "Color": "Green"})

@routes.get('/api/stop')
async def get_stop_handler(request):
    global loop
    loop.stop()
    await ct.StopAnimation()
    
    return web.json_response({"Status": "Off", "Color": "Clear"})

@routes.get('/api/loop')
async def get_loop_handler(request):
    await ct.StartAnimation()
    asyncio.ensure_future(__initEffectLoop())
    
    return web.json_response({"Status": "On", "isLooping": True})

@routes.get('/api/color/change/{color}')
async def post_changeColor_handler(request):
    colorCode = request.match_info.get('color', '#0F0').lstrip("#")

    rgb = tuple(int(colorCode[i:i+2], 16) for i in (0, 2, 4))
    
    print("Color: " + str(rgb))
    await ct.TreeColor(ct.getColor(rgb), [])
    
    return web.json_response({"Color": colorCode})

@routes.get('/api/delayUp')
async def get_delayUp_handler(request):
    await ct.IncreaseDelay()
    
    return web.json_response({"Delay": "Up"})

@routes.get('/api/delayDown')
async def get_delayDown_handler(request):
    await ct.DecreaseDelay()
    
    return web.json_response({"Delay": "Down"})

@routes.get('/api/brightnessUp')
async def get_brightnessUp_handler(request):
    await ct.IncreaseBrightness()
    
    return web.json_response({"Brightness": "Up"})

@routes.get('/api/brightnessDown')
async def get_brightnessDown_handler(request):
    await ct.DecreaseBrightness()
    
    return web.json_response({"Brightness": "Down"})

### Default Route Handler
@routes.get("/")
async def default_route_handler(request):
    return web.FileResponse(currentdir + '/build/index.html')

app.add_routes(routes)
app.router.add_static("/", currentdir + "/build")

if __name__ == '__main__':
    print("Starting web app")
    web.run_app(app, port=serverPort)