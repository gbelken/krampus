import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


import asyncio
import constants
from aiohttp import web
from ChristmasTree import ChristmasTree

hostName = "localhost"
serverPort = 8080
isloop = False

ct = ChristmasTree() #Using Defaults
count = 0
colors = [{'name': 'rainbow', 'colors': constants.rainbowColors}, 
          {'name': 'halloween', 'colors': constants.halloweenColors},
          {'name': 'christmas', 'colors': constants.christmasColors}]


def findPalette(color):
    result = [palette for palette in colors if palette["name"] == color]
    return result

colorPalette = constants.rainbowColors

print("color: " + str(findPalette("halloween")))

sequenceLoop = []

currentSequence = ""

async def effectWorker():
    global count
    global currentSequence
    while isloop:
        for effect in sequenceLoop:
            currentSequence = effect
            if effect == "RainbowTree":
                await ct.RainbowTree(colorPalette)
            else:
                await ct.colorIterator(colorPalette, ct.__getattribute__(effect))
            await asyncio.sleep(0)
        
        count += 1
        print("Effects Loop Count: " + str(count))

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
    data = { "isLooping": isloop, 
            "Count": count, 
            "SequenceLoop": sequenceLoop, 
            "CurrentSequence": currentSequence }
    return web.json_response(data)

@routes.get('/api/start')
async def get_start_handler(request):
    await ct.StartAnimation()
    await ct.TreeColor(ct.getColor(constants.GREEN))
    return web.json_response({"Status": "On", "Color": "Green"})

@routes.get('/api/stop')
async def get_stop_handler(request):
    await ct.StopAnimation()
    global isloop
    isloop = False
    return web.json_response({"Status": "Off", "Color": "Clear"})

@routes.get('/api/loop')
async def get_loop_handler(request):
    global isloop
    isloop = True
    await ct.StartAnimation()
    asyncio.ensure_future(__initEffectLoop())
    
    return web.json_response({"Status": "On", "isLooping": isloop})

@routes.get("/api/color")
async def get_colors_handler(request):
    return web.json_response(colors)

@routes.get('/api/color/change/{color}')
async def post_changeColor_handler(request):
    global colors
    global colorPalette
    colorName = request.match_info.get('color', 'rainbow')
    selectedPallete = findPalette(colorName)

    if selectedPallete and len(selectedPallete) > 0:
        colorPalette = selectedPallete[0]['colors']
    
    return web.json_response({"Color": colorName})

@routes.post("/api/sequence")
async def post_seq_handler(request):
    global sequenceLoop
    global isloop
    requestJson = await request.json()
    print(requestJson)
    if (requestJson["sequence"]):
        sequenceLoop.append(requestJson["sequence"])

    return web.json_response({ "isLooping": isloop, "sequence": sequenceLoop })
    

### Default Route Handler
@routes.get("/")
async def default_route_handler(request):
    return web.FileResponse(currentdir + '/index.html')

app.add_routes(routes)
app.router.add_static("/", currentdir)

if __name__ == '__main__':
    print("Starting web app")
    web.run_app(app)