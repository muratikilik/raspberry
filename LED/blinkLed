## 2015 Murat Ikilik <muratikilik@yandex.com.tr>
## Raspberry Pi with "BlinkLed" project

#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

led = 11
GPIO.setup(led, GPIO.OUT)

while True:
  GPIO.output(led, GPIO.HIGH)
  time.sleep(1)
  GPIO.output(led, GPIO.LOW)
  time.sleep(1)
  
GPIO.cleanup()
