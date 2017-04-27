
import serial
from time import sleep
class CommandArduino: # Clase comando para indicar los comandos neesarios del robot
	
	def __init__(self, code, times, serial1):
		self.code = code
		self.times = times
		self.serialDev = serial1
		print("command created ") #quitar primer comentario para debuggear
	def send(self):
		print("send") #DEBUG
		self.serialDev.flushInput()
		self.serialDev.flushOutput()
		for i in range(0, self.times):
			self.serialDev.write(self.code)
			sleep(0.5)
			print("Sent : " + self.code)
			res = 0
			while res ==0:
##				while self.serialDev.inWaiting() <= 0:
##					print self.serialDev.inWaiting()
##					pass
##				res = self.serialDev.read(1)
				res = self.serialDev.readline()
				print(res + " OK")
				if(res != self.code):
					self.serialDev.write(self.code)
				return res
	def setTimes(self, times):
		self.times = times
