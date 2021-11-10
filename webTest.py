# Python 3 server example
from ChristmasTree import ChristmasTree
import constants
from aiohttp import web
import asyncio

hostName = "localhost"
serverPort = 8080
isloop = False

ct = ChristmasTree("d18", 350)
count = 0
colorPallete = constants.rainbowColors

async def treeWorker():
    global count
    while isloop:
        
        await ct.colorIterator(colorPallete, ct.strandRotator)
        await ct.colorIterator(colorPallete, ct.bottomUp)
        await ct.colorIterator(colorPallete, ct.treeSpiral)
        await ct.colorIterator(colorPallete, ct.treeColor)
        await asyncio.sleep(0)
        count += 1
        print("Tree loop count: " + str(count))

loop = asyncio.get_event_loop()



async def TreeLoop():
    try:
        asyncio.ensure_future(treeWorker())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing Loop")
        loop.close()


async def handle(request):
    command = request.match_info.get('command', "Anonymous")
    global isloop
    global count
    if command == 'start':
        ct.StartAnimation()
        await ct.treeColor(ct.getColor(constants.GREEN))
        return web.Response(text="Tree On (Green)")
    elif command == 'stop':
        isloop = False
        await ct.StopAnimation()
        return web.Response(text="Tree off")
    elif command == 'rainbow':
        print("rainbow")
        asyncio.create_task(ct.colorIterator(constants.rainbowColors, ct.strandRotator))
        print("called after rainbow function")
        return web.Response(text="Rainbow engage")
    elif command == "loop":
        isloop = True
        ct.StartAnimation()
        asyncio.ensure_future(TreeLoop())
        print("Tree Looping")
        return web.Response(text="Tree Loop Engaged")
    elif command == "colorChange":
        print("Change Color")
        global colorPallete
        if colorPallete == constants.rainbowColors:
            colorPallete = constants.halloweenColors
        else:
            colorPallete = constants.rainbowColors
        return web.Response(text="ColorChanged")
    elif command == "status":
        return web.Response(text="Tree Looping: " + str(isloop) + " count: " + str(count))

app = web.Application()

app.add_routes([web.get('/api', handle),
               web.get('/api/{command}', handle)])

app.router.add_static("/", "")

if __name__ == '__main__':
    print("Starting web app")
    web.run_app(app)
