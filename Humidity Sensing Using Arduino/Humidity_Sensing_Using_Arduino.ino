#include "DHT.h"
#define DHTPIN 8     
#define DHTTYPE DHT11   
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
  Serial.println("Starting the sensor...");
  delay(1500);
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  float f = dht.readTemperature(true);
 if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println(F("Cannot read from DHT Sensor attached..."));
    return;
  }
 float heat_index_f = dht.computeHeatIndex(f, h);
 float heat_index_c = dht.computeHeatIndex(t, h, false);
  Serial.print(F("Humidity: "));
  Serial.print(h);
  Serial.print(F("%  Temperature: "));
  Serial.print(t);
  Serial.print(F("°C "));
  Serial.println(f);

  delay(2000);
}
