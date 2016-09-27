#include <NewPing.h>
#include <ZumoMotors.h>

#define TRIGGER_PIN  2
#define ECHO_PIN     4
#define MAX_DISTANCE 600

NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);
ZumoMotors motors;
long duration, distance;

void setup() {
  pinMode(13, OUTPUT);
  pinMode(TRIGGER_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  Serial.begin(9600);
}

void loop() {
  
  digitalWrite(TRIGGER_PIN, LOW); 
  delayMicroseconds(2); 

  digitalWrite(TRIGGER_PIN, HIGH);
  delayMicroseconds(10); 
 
  digitalWrite(TRIGGER_PIN, LOW);
  duration = pulseIn(ECHO_PIN, HIGH);
 
  //Calculate the distance (in cm) based on the speed of sound.
  distance = duration/58.2;
  
  Serial.println(distance);
  motors.setRightSpeed(100); 
  motors.setLeftSpeed(100);
  delay(200);
  
  if(distance <= 15) {    
            
    digitalWrite(13, HIGH);  // turn the other way

    motors.setLeftSpeed(-300);
    motors.setRightSpeed(100);
 
    delay(200);
    digitalWrite(13, LOW);
    
  }   
}
