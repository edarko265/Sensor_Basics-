import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
x=int(input("how many time do you want the light to be lit up?"))
y=int(input("type 1 for yellow LED and 2 for green LED"))

if y==1:
    led=11
else :
    led=13
for i in range(x):
    GPIO.output(led,True)
    time.sleep(1)
    GPIO.output(led,False)
    time.sleep(1)



GPIO.cleanup()

