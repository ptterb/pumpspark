from __future__ import division
import serial
import time


ser = serial.Serial('/dev/tty.usbserial-DAWR134X')
print ser.portstr


def send(pump, level):
	ser.write(chr(255))
	ser.write(chr(pump))
	ser.write(chr(level))

def main():	
    send(0,0)
    send(3,254)
    time.sleep(2)
    send(3,0)
    time.sleep(1)
    ser.close()

if __name__ == '__main__':
	main()
	
