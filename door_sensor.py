import RPi.GPIO as GPIO
import time

def magnectic(door_sensor_pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(door_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    wtime = 0.5

    try:
        while True:
            door_state = GPIO.input(door_sensor_pin)
            if door_state == GPIO.LOW:  # closed
                return False
            else:  # opened
                return True
            time.sleep(wtime)  

    except KeyboardInterrupt:
        pass

    finally:
        GPIO.cleanup()

# door_sensor_pin = 17
