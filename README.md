<h1 align="center">
  <img src="https://github.com/semicolon123/INTRU-INFI-TH101/blob/master/Images/Project%20Image.jpg" alt="INTRU-INFI-TH101">
  <br>
  Intruder Detection and Agriculture Information System (INTRU-INFI-TH101)
</h1>

Now-a-days, farmers increasingly face the problem of trespassing and lack of information during agricultural practices. Our project tries to address this issue by using the IR sensor for the detection of intruder(s). We are also using the temperature and humidity sensor so that farmer has knowledge about his fields and can plan accordingly. The temperature and humidity values are stored in a file and the same is uploaded on cloud servers. This data is used for future forecasting for the farmer. An app shall be used by farmer to get the stats based on historic data stored on cloud.

A database is also maintained that stores the contact information of the farmer. This contact is retrieved by the program and is used by GSM to send sms to the intended recipient (the farmer). File handling has been employed to store the temperature and humidity in a file which shall be further uploaded on cloud.



#### COMPONENTS USED

1. Raspberry Pi

2. DHT11 (Temperature and Humidity Sensor)

3. GSM Module 900A

4. Infrared (IR) sensor

5. Power supply Unit

#### PROJECT SCREENSHOTS AND OUTPUT
<h4 align="center"><img src="https://github.com/semicolon123/INTRU-INFI-TH101/blob/master/Images/Demo%20gif.gif" alt="INTRU-INFI-TH101 sms2">
<br> 
  Working Project Demo 
</h4>
<h4 align="center"><img src="https://github.com/semicolon123/INTRU-INFI-TH101/blob/master/Images/sms2.png" alt="INTRU-INFI-TH101 sms2" width="400" height="500">
  <br>
  Sample SMS received by the farmer as per the condition
  <h4>


#### STEPS TO RUN THE PROJECT

● First of all  run the file named '1ask_user_no'. It will ask users to enter his/her mobile number.

● After this one can run file named '2sendmsg'. This code will send a message to the farmer as soon as the IR sensor senses an intruder in the field.

● Run the file namely 'finaltemp1' to activate the temperature and humidity sensor and record the field’s temperature and humidity. 
Accordingly a message is sent to the farmer.

