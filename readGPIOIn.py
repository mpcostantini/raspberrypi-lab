#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from optparse import OptionParser
import json

class GPIOReader:

  @classmethod
  def init_option_parser(cls):
    parser = OptionParser()
    parser.add_option("-i", "--gpioin", action="store", type="int", dest="gpioin", default=4, help="GPIO number where INPUT device is connected")
    parser.add_option("-f", "--jsonfile", action="store", type="string", dest="jsonoutputfile", default="gpio-events.json", help="JSON File for commands read from GPIO")
    (options, args) = parser.parse_args()
    return options

  def __init__(self):
    self.last_event_time = time.time()
    self.options = GPIOReader.init_option_parser()    
    self.json_file = self.options.jsonoutputfile
    self.out_json_file = open(self.json_file, 'w')
    self.init_gpio()

  def log_input(self, channel):
    new_event_time = time.time()
    elapsed_time = new_event_time - self.last_event_time
    if GPIO.input(channel) == GPIO.HIGH:
      print 'Input turned ON after {} seconds'.format(elapsed_time)
      json.dump({'source': 'gpio', 'value': True, 'time' : elapsed_time}, self.out_json_file)
    else:
      print 'Input turned OFF after {} seconds'.format(elapsed_time)
      json.dump({'source': 'gpio', 'value': False, 'time' : elapsed_time}, self.out_json_file)
    self.last_event_time = new_event_time
    self.out_json_file.write('\n')

  def init_gpio(self):
    GPIO.setmode(GPIO.BCM)	
    GPIO.setup(self.options.gpioin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(self.options.gpioin, GPIO.BOTH, callback=self.log_input, bouncetime=200)

  def wait_events_loop(self):
    i = 0
    while True:
      i = i + 1
      print(i)
      time.sleep(1)	

  def end(self):
    print 'Exiting readGPIOIn. Doing GPIO cleanup.'
    GPIO.cleanup()

try:
  gpio_reader = GPIOReader()
  gpio_reader.wait_events_loop()
except KeyboardInterrupt:
  gpio_reader.end()

