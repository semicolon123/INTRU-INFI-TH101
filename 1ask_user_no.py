from Tkinter import *
import time
import MySQLdb
db=MySQLdb.connect("localhost", "alka", "root", "group13")       #cinfo is username, new is database name 

def get_no():
	phoneNum=e1.get()
	curs=db.cursor()
	curs.execute("INSERT INTO contact(phoneNum) VALUES(%s)",(phoneNum))
	db.commit()

master=Tk()
Label(master,text="Enter Your Number:").grid(row=0)
e1=Entry(master)
e1.grid(row=0, column=1)
Button(master, text='Quit', command=master.quit).grid(row=3,column=0,sticky=W, pady=4)
Button(master, text='Submit', command=get_no).grid(row=3, column=1, sticky=W, pady=4)
mainloop()

	
