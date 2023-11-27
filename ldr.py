# import RPi.GPIO as GPIO  
from statistics import mean
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from time import sleep

# GPIO.setmode(GPIO.BCM) 
# GPIO.setup(18, GPIO.IN)


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

# True = the connection is still good
# False = the connection is broken
wait_time = 5
def CheckIfTheLaserBroken(chan):
    value = average(chan) 
    if(value > 40):
        return True
    else:
        return False 


def average(chan):
    arr = [] 
    for i in range(1000):
        arr.append(chan.value)
        sleep(0.00001)

    aver=mean(arr)
    return aver

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


while True: 
    # # print("1:", chan1.value)
    # # sleep(0.5)
    # print("2:", chan2.value)
    # print("-----")
    # print(CheckIfTheLaserBroken(chan1), " + " ,CheckIfTheLaserBroken(chan2))
    # print(movement_detect())

    # print(GPIO.input(18))
    # print("chan1: ",average(chan1), " + chan2: ",average(chan2))
    # print("chan1: ",average(chan1))
    # print("chan2: ",average(chan2))
    sleep(0.1)   
