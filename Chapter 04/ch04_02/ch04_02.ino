
#include <ZumoMotors.h>
#include <SoftwareSerial.h>

// D2   >>>  Rx, D4   >>>  Tx
SoftwareSerial bluetooth(2, 4); // RX, TX
char val;
ZumoMotors motors;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);  
  bluetooth.begin(9600);  
  Serial.println("Bluetooth On..");
}

void loop() {
  if(bluetooth.available()){
    digitalWrite(13, HIGH);
    val = bluetooth.read();
    
      Serial.println(val);
    if( val == 'l' ) {  
      motors.setLeftSpeed(-300);
      motors.setRightSpeed(100);    
      Serial.println("turn left");
    }
    if( val == 'r' ) {  
      motors.setRightSpeed(-300);
      motors.setLeftSpeed(100);    
      Serial.println("turn right");
    }
    if( val == 'f' ) {  
      motors.setLeftSpeed(100);
      motors.setRightSpeed(100);    
      Serial.println("forward");
    }
    
    digitalWrite(13, LOW);
    
  }
  
  delay(200);  
}
