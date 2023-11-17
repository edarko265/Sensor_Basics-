import RPi.GPIO as GPIO
import time
import pygame

def playsound():
    pygame.mixer.init()
    buzzer= pygame.mixer.Sound("alarm.mp3")
    playing= buzzer.play()


def stop_play():
    pass

# while playing.get_busy():
#     pygame.time.delay(100)