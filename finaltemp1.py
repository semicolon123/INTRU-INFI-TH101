import Adafruit_DHT
import time
import serial
sensor=Adafruit_DHT.DHT11
import MySQLdb
db=MySQLdb.connect("localhost", "alka", "root", "group13")       #alka is username, group13 is database name
cur=db.cursor()
pin=24
x=[1]
for i in x:
        print '\n'
        print '*****TEMPERATURE AND HUMIDITY SENSOR ACTIVATED*****'
        time.sleep(1)
        print '\n'
	hum,temp=Adafruit_DHT.read_retry(sensor,pin)
        f=open("tfile.txt",'a')
	f.write("Recorded at: ")
	f.write(time.strftime("%H:%M:%S"))      #time of recording
	f.write("\t")
	f.write(time.strftime("%d/%m/%y"))      #date of recording
	f.write("\n")
	f.write("Temperature="+str(temp))
        f.write("\n")
	f.write("Humidity="+str(hum))
	
        if hum is not None and temp is not None:
                time.sleep(2)
		print 'Temp={0:0.1f}*C hum={1:0.1f}%'.format(temp,hum)
		time.sleep(2)
		if temp==20:
                        msg1="Fit for layer bird."

                elif temp>20 or temp<20:
                        msg1="Layer bird can't breed."


                if (temp>30 or temp<=40) and (hum>60 or hum<80):
                        msg2="Fit for broiler breeding."

                else:
                        msg2="Unfit for broiler breeding."
                                          #second type of check has been performed for the wheat and wheat- type crop kernel

                if (hum>33 or hum<=43) and (temp>33 or temp<=43):
                        msg3="Fit for wheat cultivation."
                else:
                        msg3="Too high."
                        break
                f.write("\n")
                f.write(msg1)
                f.write("\t")
                f.write(msg2)
                f.write("\t")
                f.write(msg3)
                f.write("\n")
                f.write("\n")
                
                try:
			port=serial.Serial("/dev/ttyS0",9600,timeout=3.0)
		        print '\n'
			print "GSM SIM9600 Working\n"
			print "OK"
			#print"AT to check operation"
			port.write('AT\r\n')
			rcv=port.read(20)
			#print"GSM Working:"+rcv
	        	rcv=port.read(20)
			cur.execute("SELECT phoneNum FROM contact") 
			for row in cur.fetchall():
				number=str(row[0])		#row=no of attributes
				print"Message passed to the farmer"
				port.write('AT+CMGS="'+number+'"\r\n')
				time.sleep(1)

				port.flushInput()
				port.flushOutput()
				port.write(msg1)
				port.write(msg2)
				port.write(msg3)
                                time.sleep(1)
				port.write('\x1A\r\n')
				#print port.read(50)
				port.flushInput()
				port.flushOutput()
                except:
			port.close()
	 

        else:
                print'failed to get ready'
