import door_sensor
import ldr
import sharp
import Speaker

while True:
    if(door_sensor.magnetic()==False): #the door is closed
        pass
    else: #the door is opened
        match ldr.movement_detect():
            case 0: #no movement detected. Do it later
                pass
            case 1: #Outward movement detected.Eric's part
                pass
            case 2: #Inward movement detected. Vincent's part
                pass

