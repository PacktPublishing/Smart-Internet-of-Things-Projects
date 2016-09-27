#include <WiFi101.h>
#include <ArduinoCloud.h>
#include "DHT.h"

/////// Wifi Settings ///////
char ssid[] = "<your_ssid>";
char pass[] = "<your_ssid_password";


// Arduino Cloud settings and credentials
const char userName[]   = "<your_thing_username>";
const char thingName[] = "<your_thins_name>";
const char thingId[]   = "<your_thing_id>";
const char thingPsw[]  = "<your_thing_password>";


WiFiSSLClient sslClient;


// build a new object "arduinobot"
ArduinoCloudThing arduinobot;


// define DHT22
#define DHTTYPE DHT22 
// define pin on DHT22
#define DHTPIN 8 

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin (9600);

  dht.begin();

  // attempt to connect to WiFi network:
  Serial.print("Attempting to connect to WPA SSID: ");
  Serial.println(ssid);

  while (WiFi.begin(ssid, pass) != WL_CONNECTED) {
    // unsuccessful, retry in 4 seconds
    Serial.print("failed ... ");
    delay(4000);
    Serial.print("retrying ... ");
  }
  Serial.println("connected to wifi");

  arduinobot.begin(thingName, userName, thingId, thingPsw, sslClient);
  arduinobot.enableDebug();

  // define the properties
  arduinobot.addProperty("Humidity", FLOAT, R);
  arduinobot.addProperty("Temperature", FLOAT, R);
}

void loop() {

  arduinobot.poll();

  delay(2000);

  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  arduinobot.writeProperty("Temperature", t);
  arduinobot.writeProperty("Humidity", h);    
  delay(1000);
  
}

