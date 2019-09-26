#!/usr/bin/env python

import cgi
import cgitb    #display CGI error on browser
import time
import RPi.GPIO as GPIO
import sys

print('Content-type: text/html; charset=UTF-8\r\n')
print('Web Servo')

print('<form action="" method="post">')
print('<input type="number" name="degree">')
print('<input type="submit" name="submit" value="submit">')
print('</form>')

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

bottom = 2.5
middle = 7.2
top = 12.0

form = cgi.FieldStorage()
if form.has_key("degree"):
    print('<script>')
    print('console.log(' + '"hoge"' + ')')
    print('</script>')
    value = float(form.getvalue("degree"))
    servo.ChangeDutyCycle(middle + (12.0-7.2)*(value/90.0))
time.sleep(1)
