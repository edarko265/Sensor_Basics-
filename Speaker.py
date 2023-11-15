import RPi.GPIO as GPIO
import time
import pygame

pygame.mixer.init()
buzzer = pygame.mixer.Sound("alarm.mp3")

def playsound():
    playing = buzzer.play()
    while playing.get_busy():
        pygame.time.delay(100)

def stop_playsound():
    playing = buzzer.play()
    if playing.get_busy():
        playing.stop()

#playsound()
#time.sleep(5) 
#stop_playsound()
