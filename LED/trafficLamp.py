## 2015 Murat Ikilik <muratikilik@yandex.com.tr>
## Raspberry Pi with "Traffic Lamp" project

#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

redLed = 11
yellowLed = 12
greenLed = 13

number1 = 0
number2 = 0

GPIO.setup(redLed, GPIO.OUT)
GPIO.setup(yellowLed, GPIO.OUT)
GPIO.setup(greenLed, GPIO.OUT)

GPIO.output(redLed, 1)
GPIO.output(yellowLed, 1)
GPIO.output(greenLed, 1)

number2 = int(raw_input("Dongu sayisini girin: "))

while number1<number2:
  GPIO.output(redLed, GPIO.HIGH)
  GPIO.output(yellowLed, GPIO.LOW)
  GPIO.output(greenLed, GPIO.LOW)
  time.sleep(3)
  
  GPIO.output(redLed, GPIO.LOW)
  GPIO.output(yellowLed, GPIO.HIGH)
  GPIO.output(greenLed, GPIO.LOW)
  time.sleep(2)
  
  GPIO.output(redLed, GPIO.LOW)
  GPIO.output(yellowLed, GPIO.LOW)
  GPIO.output(greenLed, GPIO.HIGH)
  time.sleep(3)
  
  number1 += 1
  
GPIO.cleanup()
