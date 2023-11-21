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
chan1 = AnalogIn(mcp, MCP.P1) #outside of the house
chan2 = AnalogIn(mcp, MCP.P2) #inside of the house

normal_value = 0

wait_time = 5
def CheckIfTheLaserBroken(chan): 
    if(chan.value < 100):
        return False #the connection has been broken
    else:
        return True #the connection is still good


def movement_detect():
        if((CheckIfTheLaserBroken(chan1) == True) and (CheckIfTheLaserBroken(chan2) == True)):
            return 0 #Nothing
        elif (CheckIfTheLaserBroken(chan2)==False):
            return 1 #outward movement , inside of the house
        elif (CheckIfTheLaserBroken(chan1)==False): 
            return 2 #inward movement , outside of the house


# while True: 
#     # print(chan2.value)
#     # print(CheckIfTheLaserBroken(chan1))
#     print(movement_detect())
#     sleep(1)   
