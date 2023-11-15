import RPi.GPIO as GPIO
import time

def magnectic(door_sensor_pin=17): #def magnectic(door_sensor_pin=17, speaker_pin=18):
    # Set up GPIO
    GPIO.setmode(GPIO.BCM)

    # GPIO input for magnectic
    GPIO.setup(door_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # GPIO output for speaker
    #GPIO.setup(speaker_pin, GPIO.OUT)

    try:
        while True:
            # Read the state of magnectic
            door_switch_state = GPIO.input(door_sensor_pin)

            if door_switch_state == GPIO.LOW:
                # door switch is open, turn on the speaker
                #GPIO.output(speaker_pin, GPIO.LOW)
                return False
                #print("door switch is closed - Speaker OFF")
                
            else:
                # door switch is closed, turn off the speaker
                return True
                #GPIO.output(speaker_pin, GPIO.HIGH)
                #print("door switch is opened - Speaker ON")
                #play_buzzer()
               
            time.sleep(0.5)  # Adds a small delay to avoid rapid change of state

    except KeyboardInterrupt:
        # Clean up GPIO on keyboard interrupt CTRL+C
        print("Keyboard interrupt detected. Cleaning up GPIO.")
        GPIO.cleanup()
        print("Exiting the program.")

# Uncomment the following line if you want to run this script independently
#magnectic()

#code to call it in another file
# from door_sensor import magnectic

# Call the function with the desired GPIO pins
#magnectic(door_sensor_pin=17, speaker_pin=18)