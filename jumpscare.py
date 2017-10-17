# This Code Triggers a video to play on 
# the raspberry pi when motion is detected 
# via a PIR sensor on BCM pin 5. # Written By 
# Charles Gantt 2017
# http://www.themakersworkbench.com
# & http://www.youtube.com/c/themakersworkbench
# https://github.com/CharlesJGantt/Smart-Mirror-With-Halloween-Jump-Scare

import RPi.GPIO as GPIO
import time
import os
import sys

from subprocess import Popen

GPIO.setmode(GPIO.BCM)

movie1 = ("/home/pi/Smart-Mirror-With-Halloween-Jump-Scare/zombie.mp4")

GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(26, GPIO.OUT)
motionDetected = 0

while True:
    input_state = GPIO.input(5)
    if input_state == True:
        print('Motion Detected')
        motionDetected += 1
        time.sleep(0.2)
    if motionDetected == 1:
        GPIO.output(26, GPIO.HIGH)
        os.system('killall omxplayer.bin')
        omxc = Popen(['omxplayer', '-b', movie1])
        player = True
        time.sleep(60)
        motionDetected = 0
        GPIO.output(26, GPIO.LOW)
