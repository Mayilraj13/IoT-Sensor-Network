int const trigPin = 9;
int const echoPin = 10;
int const buzzPin = 0;
void setup()
{
pinMode(trigPin, OUTPUT); 
pinMode(echoPin, INPUT); 
pinMode(buzzPin, OUTPUT); 
}
void loop()
{

int duration, distance;
digitalWrite(trigPin, HIGH);
delay(1);
digitalWrite(trigPin, LOW);
duration = pulseIn(echoPin, HIGH);
distance = (duration/2) / 29.1;
if (distance <= 100 && distance >= 0) {

digitalWrite(buzzPin, HIGH);
} else {
digitalWrite(buzzPin, LOW);
}
delay(60);
}
