from __future__ import division
import serial
import time


ser = serial.Serial('/dev/tty.usbserial-DAWR134X')
print ser.portstr


def send(pump, level):
	ser.write(chr(255))
	ser.write(chr(pump % 8))
	ser.write(chr(level % 254))

def sendstream(delay, pump, *args):
	'''
	Specify delay in ms, and stream
	'''
	for x in args:
		send(pump,x)
		time.sleep(max(100, delay)/1000)


def run_pump():
	#Do your thing
	sendstream(100, 0, 200,0,0,0,200,0)
	sendstream(100, 2, 200,0,0,0,200,0)
	sendstream(100, 3, 200,0,0,0,200,0)
	sendstream(100, 1, 200,0,0,0,200,0)
	pass

def main():
	run_pump()
	# Killemall
	for x in xrange(0,7):
		send(x,0)
	ser.close()

if __name__ == '__main__':
	main()
	