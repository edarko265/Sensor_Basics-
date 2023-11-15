# import RPi.GPIO as GPIO
# import time
# import pygame
# import digitalio
 
     
'''pygame.mixer.init()
buzzer= pygame.mixer.Sound("alarm.mp3")

playing= buzzer.play()
while playing.get_busy():
    pygame.time.delay(100)'''
  
"""GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)


x=int(input("how many time do you want the light to be lit up?"))
y=int(input("type 1 for yellow and 2 for green"))

if y==1:
   led=11  
else :
   led=13
for i in range(x):
    time.sleep(1)
    GPIO.output(led,True)
    time.sleep(1)

GPIO.cleanup()"""

import time
import keyboard

start_time = time.time()  # Start the timer
key_pressed = False

while True:
    if keyboard.is_pressed("s"):
        key_pressed = True
        break
    elif time.time() - start_time >= 5:
        print("nothing happen")
        break

if key_pressed:
    print("it has been pressed")