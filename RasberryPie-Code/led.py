import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
from firebase import firebase
from firebase_admin import db
from firebase.firebase import FirebaseApplication
from firebase.firebase import FirebaseAuthentication
import json

#firebase details
config = {

  "apiKey": "JQTcsq6HNfJlZyx30iPJOCOw93YHI1AE8QRyBnBv",

  "authDomain": "arduinofirebaseconnectio-d58e9.firebaseapp.com",

  "databaseURL": "https://arduinofirebaseconnectio-d58e9-default-rtdb.firebaseio.com",

  "storageBucket": "arduinofirebaseconnectio-d58e9.appspot.com",

 # "serviceAccount": "path/to/serviceAccountCredentials.json"

}

#GPIO settings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

bulb1 = 17
bulb2 = 27
bulb3 = 22
bulbdefault = 0

#Output Pin setup
GPIO.setup(bulbdefault,GPIO.OUT)
GPIO.setup(bulb1,GPIO.OUT)
GPIO.setup(bulb2,GPIO.OUT)
GPIO.setup(bulb3,GPIO.OUT)
#GPIO.setup(bulb1,GPIO.OUT)


#Connecting with Firebase
print("Connecting with the Server......")
auth = FirebaseAuthentication(config['apiKey'],'officialharshitpant@gmail.com',True,True)
firebase = FirebaseApplication(config['databaseURL'],auth)
print(firebase)



#firebase.get_child('reply','0')

lights = {
    
    'Bulb1': bulb1,
    'Bulb2': bulb2,
    'Bulb3': bulb3,
    'Bulb4': 0,
    'Bulb5': 0,
    }

GPIO.output(bulb1,0)
#firebase.push('moistureBoolean',json.dumps('1'))
#core function
def get_data():
    
    all_lights = firebase.get('Bulbs/',None)
    print(all_lights)
    
    for i in all_lights:
       
        if int(all_lights[i]) == 1:
            #print("light type =",type(lights[i]))
            GPIO.output(lights[i],GPIO.HIGH)  
        if int(all_lights[i]) == 0:
            GPIO.output(lights[i],GPIO.LOW) 
        
    
	#L1 = firebase.get('Bulb1',None)
	#print(L1)
	#if L1 =='1':
	#	GPIO.output(output_pin,GPIO.HIGH)
	#	firebase.put('https://arduinofirebaseconnectio-d58e9-default-rtdb.firebaseio.com','reply','1')
	#	
	#else:
	#	GPIO.output(output_pin,GPIO.LOW)
	#	firebase.put('https://arduinofirebaseconnectio-d58e9-default-rtdb.firebaseio.com','reply','0')

#main loop
while True:
	get_data()
