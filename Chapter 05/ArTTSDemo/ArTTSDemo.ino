#include <SoftwareSerial.h>  
#include "EMIC2.h"

// Read here: http://arduino.cc/en/Reference/SoftwareSerial
#define RX_PIN 9  // Connect SOUT Emic 2 module to the RX pin
#define TX_PIN 8  // Connect SIN Emic 2 module to the TX pin

EMIC2 emic; 

void setup() {  
  emic.begin(RX_PIN, TX_PIN);    
  emic.setVoice(8);  // Sets the voice (9 choices: 0 - 8)

}

void loop() {
  // put your main code here, to run repeatedly:
  emic.setVolume(10);
  emic.speak("Hello Arduino");
  emic.resetVolume();
  delay(2000);

  emic.speak("I am waiting your command");
  delay(3000);

}
