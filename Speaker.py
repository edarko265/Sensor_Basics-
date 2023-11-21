import RPi.GPIO as GPIO
import time
import pygame
import random
import ldr
import sharp

#list of MP3 file paths
ryme_voices = ["sound1.mp3", "sound4.mp3"]
pygame.mixer.init()
random_file = random.choice(ryme_voices)
buzzer = pygame.mixer.Sound(random_file)
buzzer.set_volume(0.4)

def playsound():
    # Play the sound
    time.sleep(1) 
    while True:
        playing = buzzer.play()
        while playing.get_busy():
            pygame.time.delay(100)

        # stop playing sound if somebody has walk in or the Sharp sensor sense someone
        if (ldr.movement_detect()==2 or sharp.presence_detection()==True):
            break


while True:     
    playsound()