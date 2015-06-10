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

b = int(raw_input("Dongu sayisini girin: "))

while a<b:
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
  
  a += 1
  
GPIO.cleanup()
