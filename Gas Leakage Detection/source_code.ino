
int buz=7;	
int gs=A0;
int gasLevel=0;	
void setup()
{
  pinMode(buz, OUTPUT);
  pinMode(gs,INPUT);
}

void loop()
{
  digitalWrite(buz,LOW); 
  gasLevel = analogRead(gs);
  if(gasLevel>=100){	
  	digitalWrite(buz,HIGH);
  }
}
