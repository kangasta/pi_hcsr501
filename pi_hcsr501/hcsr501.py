from time import sleep

import pigpio

class HcSr501(object):
	def __init__(self, pin=17):
		self.__pi = pigpio.pi()
		self.__pi.set_mode(pin, pigpio.INPUT)

	def __str__(self):
		return ("Motion: " + str(self.active))

	@property
	def active(self):
		return bool(self.__pi.read(17))
