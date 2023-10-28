import RPi.GPIO as GPIO
import time
import pygame

def play_buzzer():
    pygame.mixer.init()
    buzzer = pygame.mixer.Sound("alarm.mp3")

    playing = buzzer.play()
    while playing.get_busy():
        pygame.time.delay(100)

