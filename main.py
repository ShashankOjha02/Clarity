import RPi.GPIO as GPIO
from get_emotion import get_emotions
from weather import weather
from schedule import get_schedule
from display import *

def nothing():
    pass
def display_nothing(nothing):
    pass
options = {0:nothing, 1:weather, 2:get_emotions, 3:get_schedule}
display_options = {0:display_nothing, 1:display_weather, 2:display_emotion, 3:display_schedule}

GPIO.setup(13, GPIO.OUT)
GPIO.output(13, GPIO.HIGH)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

prev_edge = 0

state = 0
ran = 0
while True:
    if GPIO.input(26) and not prev_edge:
        state += 1
        prev_edge = 1
        ran = 0
    else:
        prev_edge = 0
    if state == 4:
        state = 0
    if state != 1 and ran == 0:
        text = options[state]()
        display_options[state](text)
        ran = 1
    if ran == 0:
        text = options[state]()
        display_options[state](text)