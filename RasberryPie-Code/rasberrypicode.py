# importing lib
import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
from firebase import firebase
import json



# setting up raspberry pi GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


#connecting raspiberry pi to firebase
firebase = firebase.FirebaseApplication('https://arduinofirebaseconnectio-d58e9-default-rtdb.firebaseio.com/', None)

#setting the input pin(4) Real: PIN-7
GPIO.setup(4,GPIO.IN)


#function to send data
def update_firebase():

	moisture= GPIO.input(4)
	print(moisture)
	if moisture is not None:
		print("Sending the data......")
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		
		z = {
			"Name": "Harshit",
			"now":current_time,
			"Moisture": moisture

		    }
		firebase.post('str',z)			
			
	else:
		print('Failed to get reading. Try again!')	
		sleep(10)

	
while True:
	update_firebase()
	sleep(5)
