import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
door_sensor_pin = 17

GPIO.setup(door_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
wtime = 0.5
def magnetic():
    while True:
        door_state = GPIO.input(door_sensor_pin)
        if door_state == GPIO.LOW: #closed
            return False
            time.sleep(wtime)
        else: #opened
            return True
            time.sleep(wtime)  # You can adjust the sleep time to control the polling rate


GPIO.cleanup()
