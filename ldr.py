import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from time import sleep


# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan1 = AnalogIn(mcp, MCP.P1)
chan2 = AnalogIn(mcp, MCP.P2)

temp = 65530

wait_time = 5
def CheckIfTheLaserBroken(chan): 
    if(temp < chan.value):
        return True #the connection has been broken
    else:
        return False #the connection is still good


def CheckDirectionOfMovement():
        if(CheckIfTheLaserBroken(chan1) == True):
            return 1 #inward movement 
        elif (CheckIfTheLaserBroken(chan2)==True):
            return 2 #outward movement
        else: 
            return 3 #nothing



    
