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
            movement = 0 #Nothing
            return movement
        elif (CheckIfTheLaserBroken(chan2)==False):
            movement = 1 #outward movement , inside of the house
            return movement 
        elif (CheckIfTheLaserBroken(chan1)==False): 
            movement = 2 #inward movement , outside of the house
            return movement  


# while True: 
#     # print(chan2.value)
#     # print(CheckIfTheLaserBroken(chan1))
#     print(movement_detect())
#     sleep(1)   
