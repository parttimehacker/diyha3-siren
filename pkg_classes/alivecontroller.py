#!/usr/bin/python3

""" DIYHA Alive Controller:
    Manage a simple digital high or low GPIO LED to indicate active.
"""

# The MIT License (MIT)
#
# Copyright (c) 2020 parttimehacker@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from threading import Thread
from time import sleep
import RPi.GPIO as GPIO

class AliveController:
    """ Abstract and manage an alive GPIO LED. """

    def __init__(self, pin=18, interval=5):
        """ Initialize the ALIVE GPIO pin. """
        self.alive_pin = pin
        GPIO.setmode(GPIO.BCM)  # Broadcom pin-numbering scheme
        GPIO.setup(self.alive_pin, GPIO.OUT)  # LED pin set as output
        self.interval = interval
        self.inactive = True

    def start(self):
        """ Start the blinking LED thread """
        self.inactive = False
        led_thread = Thread(target=self.toggle_led, args=())
        led_thread.daemon = True
        led_thread.start()

    def toggle_led(self):
        """ sleep and then flash the LED """
        while True:
            if self.inactive:
                GPIO.output(self.alive_pin, GPIO.LOW)
                return
            sleep(self.interval)
            GPIO.output(self.alive_pin, GPIO.HIGH)
            sleep(0.1)
            GPIO.output(self.alive_pin, GPIO.LOW)
            sleep(0.25)
            GPIO.output(self.alive_pin, GPIO.HIGH)
            sleep(0.1)
            GPIO.output(self.alive_pin, GPIO.LOW)

    def stop(self,):
        """ Turn power off to the GPIO pin. """
        self.inactive = True