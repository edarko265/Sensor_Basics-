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
    if(door_sensor.magnectic()==False): #the door is closed
        pass
    else: #the door is opened
        match ldr.movement_detect():
            case 0: #no movement detected.
                start_time = time.time()  # Start the timer
                while True:
                    if (ldr.movement_detect()==1):
                        if(numberPeopleInside==0):
                            pass
                        else:
                            numberPeopleInside -= 1
                        
                        checkNumbPeopleInside()

                    elif(ldr.movement_detect()==2):
                        numberPeopleInside +=1
                        

                    if time.time() - start_time >= 5: #if the door left open longer than 5s but there are no movement detected then the alarm will goes off
                        #if the door has been closed then nothing happen. Fix this part!!!
                        
                        if (door_sensor.magnectic()==True):
                            Speaker.playsound()
                            numberPeopleInside = +1
                        elif(door_sensor.magnectic()==False):
                             #check for the patient presence
                            if(sharp.presence_detection()==True):
                                pass
                            elif(sharp.presence_detection()==False):
                                Speaker.playsound()
                                numberPeopleInside = +1


            case 1: #Outward movement detected.Eric's part
                if(numberPeopleInside==0):
                     pass
                else:
                    numberPeopleInside -= 1
                
                checkNumbPeopleInside()
            case 2: #Inward movement detected. Vincent's part
                numberPeopleInside = +1
                


