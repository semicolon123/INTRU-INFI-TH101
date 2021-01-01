import RPi.GPIO as GPIO
import time
import serial
import MySQLdb			#for farmer's contact no.

db=MySQLdb.connect("localhost", "alka", "root", "group13")       #cinfo is username, new is database name 
port=serial.Serial("/dev/ttyS0",9600,timeout=3.0)
cur=db.cursor()
GPIO.setmode(GPIO.BCM)

pir=23         #pin no. 16
GPIO.setup(pir,GPIO.IN)
while True:
	if GPIO.input(pir):
                print "\n"
		print"INTRUDER DETECTED!!!!!"
                print "\n"
		try:
			port=serial.Serial("/dev/ttyS0",9600,timeout=3.0)
		
			print "GSM SIM9600\n"
			print "OK"
			#print"AT to check operation"
			port.write('AT\r\n')
			rcv=port.read(20)
			#print"GSM Working:"+rcv
	        	rcv=port.read(20)
			cur.execute("SELECT phoneNum FROM contact") 
			for row in cur.fetchall():
				number=str(row[0])		#row=no of attributes
				msg1="SOMEONE JUST ENTERED THE FARM"
				print"message passed to the farmer"
				port.write('AT+CMGS="'+number+'"\r\n')
				time.sleep(1)

				port.flushInput()
				port.flushOutput()
				port.write(msg1)
                                time.sleep(1)
				port.write('\x1A\r\n')
				#print port.read(50)
				port.flushInput()
				port.flushOutput()
				exit(0)
                except:
			port.close()

		time.sleep(1)



	else:
		print"no motion"
		time.sleep(1)
		
				
				
		



			
	


