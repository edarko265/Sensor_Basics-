import RPi.GPIO as GPIO
import time
import pygame
import random

#list of MP3 file paths
ryme_voices = ["sound1.mp3", "sound4.mp3"]
pygame.mixer.init()
buzzer = None

def playsound():
    
    random_file = random.choice(ryme_voices)
    buzzer = pygame.mixer.Sound(random_file)

    # Play the sound
    playing = buzzer.play()

    while playing.get_busy():
        pygame.time.delay(100)

def stop_playsound():
    # Check if the sound is currently playing
    playing = buzzer.play()

    if playing.get_busy():
        playing.stop()
        
#playsound()
#time.sleep(5) 
#stop_playsound()
