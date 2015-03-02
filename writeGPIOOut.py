#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from optparse import OptionParser
import json

class GPIOWriter:

	@classmethod
	def init_option_parser(cls):
		parser = OptionParser()
		parser.add_option("-o", "--gpioout", action="store", type="int", dest="gpioout", default=4, help="GPIO number where OUTPUT device is connected")
		parser.add_option("-f", "--jsonfile", action="store", type="string", dest="jsoninputfile", default="gpio-events.json", help="JSON File with input commands for GPIO")
		(options, args) = parser.parse_args()
		return options

	def __init__(self):
		self.last_event_time = time.time()
		self.options = GPIOWriter.init_option_parser()
		self.json_file = self.options.jsoninputfile
		self.in_json_file = open(self.json_file, 'r')
		self.init_gpio()

	def init_gpio(self):
		GPIO.setmode(GPIO.BCM)	
		GPIO.setup(self.options.gpioout, GPIO.OUT)

	def readJsons(self):
		for jsonline in self.in_json_file:
			yield json.loads(jsonline)

	def writeGPIO(self):
		for event in self.readJsons():
			GPIO.output(self.options.gpioout, event['value'])
			time.sleep(event['time'])

	def end(self):
		GPIO.cleanup()

gpio_writer = GPIOWriter()
gpio_writer.writeGPIO()
gpio_writer.end()
