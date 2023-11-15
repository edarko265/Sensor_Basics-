import door_sensor
import ldr
import sharp
import Speaker
import time
numberPeopleInside = 1 #only  one person inside, that is the patient

def checkNumbPeopleInside():
                if (numberPeopleInside > 1):
                    pass
                elif (numberPeopleInside == 1):
                    pass
                else:
                    Speaker.playsound()

while True:
    if(door_sensor.magnetic()==False): #the door is closed
        pass
    else: #the door is opened
        match ldr.movement_detect():
            case 0: #no movement detected.
                start_time = time.time()  # Start the timer
                while True:
                    if (ldr.movement_detect()==1):
                        numberPeopleInside = - 1
                        checkNumbPeopleInside()
                        break
                    elif(ldr.movement_detect()==2):
                        numberPeopleInside = +1
                        break

                    if time.time() - start_time >= 5: #if the door left open longer than 5s but there are no movement detected then the alarm will goes off
                        #if the door has been closed then nothing happen. Fix this part!!!
                        if (door_sensor.magnetic()==True):
                            Speaker.playsound()
                            break
                        elif(door_sensor.magnetic()==False):
                             #check for the patient presence
                            if(sharp.presence_detection()==True):
                                pass
                            elif(sharp.presence_detection()==False):
                                Speaker.playsound()
                                break

            case 1: #Outward movement detected.Eric's part
                numberPeopleInside = - 1
                checkNumbPeopleInside()
                break
            case 2: #Inward movement detected. Vincent's part
                numberPeopleInside = +1
                break


