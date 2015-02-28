#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from optparse import OptionParser

class GPIOReader:

	@classmethod
	def init_option_parser(cls):
		parser = OptionParser()
		parser.add_option("-i", "--gpioin", action="store", type="int", dest="gpioin", default=4, help="GPIO number where INPUT device is connected")
		(options, args) = parser.parse_args()
		return options

	def __init__(self):
		self.options = GPIOReader.init_option_parser()    
		self.init_gpio()

	def log_input(self, channel):
		if GPIO.input(channel) == GPIO.HIGH:
			print('Input turned ON')
		else:
			print('Input turned OFF')

	def init_gpio(self):
		GPIO.setmode(GPIO.BCM)	
		GPIO.setup(self.options.gpioin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(self.options.gpioin, GPIO.BOTH, callback=self.log_input, bouncetime=300)

	def wait_events_loop(self):
		i = 0
		while True:
			i = i + 1
			print(i)
			time.sleep(1)	

	def end(self):
		GPIO.cleanup()

		
gpio_reader = GPIOReader()
gpio_reader.wait_events_loop()
gpio_reader.end()
