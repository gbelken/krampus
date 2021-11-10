import time
import random
import neopixel
import board
import constants
import asyncio


class ChristmasTree:
    """Class to control the operation of WS2811 lights"""


    def __init__(self, pin, numberOfLeds):
        print("Init ChristmasTree")
        self.pin = board.D18
        self.numberOfLeds = numberOfLeds
        self.strands = []
        self.running = True

        self.BuildStrands()

        self.pixels = neopixel.NeoPixel(
    self.pin, self.numberOfLeds, brightness=0.3, auto_write=False, pixel_order=neopixel.GRB)

    
    def BuildStrands(self):
        """Builds all the strands based on the number of pixels"""
        
        c = 0
        strand = [0] * 25
        strandCounter = 0

        for i in range(self.numberOfLeds):
            
            if strandCounter % 2 == 0:
                strand[24-c] = i
            else:
                strand[c] = i

            # Check if strand reached 25 and add to array of arrays
            if c == 24:
                self.strands.append(strand)
                strand = [0] * 25
                c = 0
                strandCounter += 1
            else:
                c+=1
    
    def StartAnimation(self):
        self.running = True
        self.pixels.brightness = 0.3
        self.pixels.show()

    async def StopAnimation(self):
        print("Stop, Turn off pixels")
        self.running = False
        #await asyncio.sleep(1)
        await self.treeColor(self.getColor(constants.CLEAR))
    
    def setPixel(self, index, color):
        if self.running:
            self.pixels[index] = color


    async def topToBottom(self, colorFunc):
        """Lights each row of lights starting from the top to the bottom"""

        for i in range(25):
            for s in self.strands:
                self.setPixel(s[i], colorFunc(i))
                #self.pixels[s[i]] = colorFunc(i)
            self.pixels.show()
            await asyncio.sleep(0.1)
    
    async def bottomUp(self, colorFunc):
        """Lights each row of lights starting from the bottom to the top"""

        for i in reversed(range(25)):
            for s in self.strands:
                #self.pixels[s[i]] = colorFunc(i)
                self.setPixel(s[i], colorFunc(i))
            
            self.pixels.show()
            await asyncio.sleep(0.1)

    async def snakeTheTree(self, colorFunc):
        """Sets the color of each bulb one by one up and down each strand of lights on to the next.  Zig-zag motion."""
        for i in range(self.numberOfLeds):
            #self.pixels[i] = colorFunc(i)
            self.setPixel(i, colorFunc(i))
            self.pixels.show()
            await asyncio.sleep(0.0001)
    
    async def treeSpiral(self, colorFunc):
        """Sets the vertical color of each strand to a single color.  Rotates thru each vertical strand setting the color"""
        for i in range(25):
            for s in self.strands:
                #self.pixels[s[i]] = colorFunc(i)
                self.setPixel(s[i], colorFunc(i))
                self.pixels.show()
                await asyncio.sleep(.0005)
    
    async def strandRotator(self, colorFunc):   
        """Iterates thru each strand and sets all the lights to the same color at the same time. Then repeats for each strand on the tree."""
        
        for strand in self.strands:
            strandColor = colorFunc(0)
            
            for pixelIndex in strand:    
                #self.pixels[pixelIndex] = strandColor
                self.setPixel(pixelIndex, strandColor)
            
            self.pixels.show()
            await asyncio.sleep(0.09)

    async def treeColor(self, colorFunc):
        
        self.pixels.fill(colorFunc(0))
        self.pixels.show()
        await asyncio.sleep(1)

    
    #Helper functions
    def randomColor(self, colors):
        return lambda index: colors[random.randint(0, (len(colors) - 1))]

    def ternary(index, option1, option2):
        if index % 2:
            return option1
        else:
            return option2

    def colorAlternator(self, color1, color2):
        return lambda index: self.ternary(index, color1, color2)

    def getColor(self, color):
        return lambda index: color

    async def colorIterator(self, colors, iteratorFunc):
        for color in colors:
            if self.running:
                await iteratorFunc(self.getColor(color))

    