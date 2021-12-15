import asyncio
import board
import constants
import neopixel
import random
import time

class ChristmasTree:
    """Class to control the operation of WS2811 lights.  Default 50 lights and GPIO pin D18 for data, segment size of 25 pixels """

    def __init__(self, pin=board.D18, numberOfLeds=500, segmentSize=25):
        self.pin = pin
        self.numberOfLeds = numberOfLeds
        self.segments = []
        self.segmentSize = segmentSize #SegmentSize is the number of lights for a vertical line of lights up and down a a tree
        self.running = True
        self.delay = 0
        self.brightness = 0.3

        self.__buildSegments()

        self.pixels = neopixel.NeoPixel(
            self.pin, self.numberOfLeds, brightness=self.brightness, auto_write=True, pixel_order=neopixel.RGB)

        print("Christmas Tree Initialized, GPIO pin: " + str(self.pin) + " Number of LEDS: " + str(self.numberOfLeds))

    def __getItem__(self, key):
        return self[key]
    
    def __setItem__(self, key, value):
        self[key] = value
    
    async def StartAnimation(self):
        self.running = True
        await self.__showPixel()

    async def StopAnimation(self):
        print("Stop, Turn off pixels")
        self.running = False

        await self.TreeColor(self.getColor(constants.CLEAR), [])

    async def IncreaseDelay(self):
        self.delay += .1
    
    async def DecreaseDelay(self):
        self.delay -= .1

    async def IncreaseBrightness(self):
        self.brightness += .1
        self.pixels.brightness = self.brightness
        self.pixels.show()
    
    async def DecreaseBrightness(self):
        self.brightness -= .1
        self.pixels.brightness = self.brightness
        self.pixels.show()
            


    ###########################################################################################################     
    ### Lighting Effects ######################################################################################
    ###########################################################################################################

    async def TopToBottom(self, colorFunc, colorCount):
        """Lights each row of lights starting from the top to the bottom"""

        if (self.running == False):
            return

        for i in range(self.segmentSize):
            for s in self.segments:
                self.__setPixel(s[i], colorFunc(i))
            self.pixels.show()
            await asyncio.sleep(0.1 + self.delay)
    
    async def BottomUp(self, colorFunc, colorCount):
        """Lights each row of lights starting from the bottom to the top"""

        if (self.running == False):
            return

        for i in reversed(range(self.segmentSize)):
            for s in self.segments:
                self.__setPixel(s[i], colorFunc(i))
            
            self.pixels.show()
            await asyncio.sleep(0.1 + self.delay)

    async def SnakeTheTree(self, colorFunc, colorCount):
        """Sets the color of each bulb one by one up and down each strand of lights on to the next.  Zig-zag motion."""
        
        for i in range(self.numberOfLeds):
            if (self.running == False):
                return

            self.__setPixel(i, colorFunc(i))
            self.pixels.show()
            await asyncio.sleep(0.0001 + self.delay)
    
    async def TreeSpiral(self, colorFunc, colorCount):
        """Sets the vertical color of each strand to a single color.  Rotates thru each vertical strand setting the color"""

        for i in reversed(range(self.segmentSize)):
            if (self.running == False):
                return

            for s in self.segments:
                self.__setPixel(s[i], colorFunc(i))
                self.pixels.show()
                await asyncio.sleep(.0005 + self.delay)

    def TestPattern(self):
        """Sets the vertical color of each strand to a single color.  Rotates thru each vertical strand setting the color"""
        print("Running Test Pattern")
        colorIndex = 0
        colors = constants.rainbowColors
        for i in reversed(range(self.segmentSize)):
            for s in self.segments:
                self.__setPixel(s[i], colors[colorIndex])
            
            self.pixels.show()
            
            colorIndex +=1

            if colorIndex > len(colors) - 1:
                colorIndex = 0
        
        time.sleep(60)
                

    async def SegmentRotator(self, colorFunc, colorCount):   
        """Iterates thru each segment and sets all the lights to the same color at the same time. Then repeats for each segment on the tree."""
        
        if (self.running == False):
            return

        for i, strand in enumerate(self.segments):
            strandColor = colorFunc(i)
            
            for pixelIndex in strand:    
                self.__setPixel(pixelIndex, strandColor)
            
            await self.__showPixel()
            await asyncio.sleep(0.09 + self.delay)

    async def RainbowTree(self, colorsFunc, colorCount):
        pixelsPerColor = int(self.numberOfLeds / colorCount)
        pixelCounter = 0
        colorIndex = 0

        if (self.running == False):
            return

        # From the bottom of the tree up, set the pixels to the colors provided, equally
        for i in reversed(range(self.segmentSize)):
            if (self.running == False):
                return
            for s in self.segments:
                self.__setPixel(s[i], colorsFunc(colorIndex))
                pixelCounter += 1
                await self.__showPixel()

                if pixelCounter >= pixelsPerColor:
                    pixelCounter = 0
                    colorIndex += 1
                
                if colorIndex > colorCount - 1:
                    colorIndex = 0

                await asyncio.sleep(.0005 + self.delay)
            
        await asyncio.sleep(1)



    async def BrightnessFlutter(self, repeatNum):
        for t in range(repeatNum):
            inten = 0.1
            for intensity in range(100):
                inten += .01
                self.pixels.brightness = inten
                self.__showPixel()
                await asyncio.sleep(.05 * (1-inten))

            for g in range(105):
                inten -= .01
                self.pixels.brightness = inten
                self.__showPixel()
                await asyncio.sleep(.05 * (1 - inten))
        await asyncio.sleep(1 )
        self.pixels.brightness = 0.3
        await self.__showPixel()

    async def TreeColor(self, colorFunc, colors):
        self.pixels.fill(colorFunc(0))
        await self.__showPixel()
        await asyncio.sleep(1)

    
    ###########################################################################################################     
    ### Helper Functions ######################################################################################
    ###########################################################################################################

    def randomColor(self, colors):
        return lambda index: colors[random.randint(0, (len(colors) - 1))], colors

    def __setPixel(self, index, color):
        """Observes the running flag on this class, it not running pixels will not get set"""
        
        if self.running:
            self.pixels[index] = color
    
    async def __showPixel(self):
        #if self.running:
        self.pixels.show()
    
    def colorByIndex(self, index, colors):
        idx = 0
        for i in range(index):
           idx += 1
           if idx >= len(colors): idx = 0
        
        return colors[idx]

    def colorAlternator(self, colors):
        return lambda index: self.colorByIndex(index, colors), colors

    def getColor(self, color):
        return lambda index: color

    async def sequenceRunner(self, sequences):
        while self.running:
            for seq in sequences:
                colorFunc, colors = self.__getattribute__(seq["colorFunc"])(seq['colors'])

                for effect in seq["effects"]:    
                    effectFunc = self.__getattribute__(effect)
                    if seq["iteratorFunc"]:
                        iteratorFunc = self.__getattribute__(seq["iteratorFunc"])
                        await iteratorFunc(seq['colors'], effectFunc)
                    else:
                        await effectFunc(colorFunc, len(colors))

    async def colorIterator(self, colors, iteratorFunc):
        for color in colors:
            if self.running:
                await iteratorFunc(self.getColor(color), len(colors))
    

    def __buildSegments(self):
        """Builds all the sections based on the number of pixels.  
        A section represents (n) number of ligts of a given strand that 
        make a vertical section on the tree"""
        
        c = 0
        segment = [0] * self.segmentSize
        pixelCounter = 0

        for i in range(self.numberOfLeds):
            if pixelCounter % 2 == 0:
                segment[(self.segmentSize - 1) -c] = i
            else:
                segment[c] = i

            # Check if strand reached segment size and add to array of arrays
            if c == (self.segmentSize - 1):
                self.segments.append(segment)
                segment = [0] * self.segmentSize
                c = 0
                pixelCounter += 1
            else:
                c+=1

if __name__ == '__main__':
    print("Starting Christmas Tree Test Pattern")
    ct = ChristmasTree()
    ca, colors = ct.colorAlternator([constants.CLEAR, constants.GREEN, constants.BLUE])
    rc, cl = ct.randomColor(constants.christmasColorsTraditional)

    effectSequence = [
        { 'id': 0, 'iteratorFunc': None, 'colorFunc': 'colorAlternator', 'effects': ['TopToBottom', 'BottomUp'], 'colors': [constants.RED, constants.GREEN] },
        { 'id': 1, 'iteratorFunc': None, 'colorFunc': 'colorAlternator', 'effects': ['SnakeTheTree', 'TreeSpiral', 'RainbowTree', 'SegmentRotator', 'TopToBottom'], 'colors': constants.christmasColorsTraditional },
        { 'id': 2, 'iteratorFunc': 'colorIterator', 'colorFunc': 'randomColor', 'effects': ['TreeColor'], 'colors': constants.christmasColorsExtended },
        { 'id': 3, 'iteratorFunc': None, 'colorFunc': 'colorAlternator', 'effects': ['SnakeTheTree', 'TreeSpiral', 'RainbowTree', 'SegmentRotator', 'TopToBottom'], 'colors': constants.christmasColorsTraditional },
        { 'id': 4, 'iteratorFunc': None, 'colorFunc': 'colorAlternator', 'effects': ['RainbowTree'], 'colors': constants.rainbowColors },
        { 'id': 5, 'iteratorFunc': None, 'colorFunc': 'colorAlternator', 'effects': ['TreeSpiral'], 'colors': [ constants.CLEAR ] },
        { 'id': 1, 'iteratorFunc': 'colorIterator', 'colorFunc': 'colorAlternator', 'effects': ['TreeSpiral'], 'colors': constants.rainbowColors },
    ]
    asyncio.run(ct.sequenceRunner(effectSequence))
