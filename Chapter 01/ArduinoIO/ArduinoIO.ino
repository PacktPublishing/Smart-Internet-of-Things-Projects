
int dig_output = 7;
int dig_input = 6;
int analog_input = A0;

int digital_val = LOW;

void setup() {
  Serial.begin(9600); 
  
  pinMode(dig_output, OUTPUT);
  pinMode(dig_input, INPUT);
}

void loop() {

  digitalWrite(dig_output,digital_val);
  int read_digital = digitalRead(dig_input);
  Serial.print("Digital write: ");
  Serial.print(digital_val);
  Serial.print(" read: ");
  Serial.println(read_digital);
  
  int ldr = analogRead(analog_input);
  Serial.print("Analog read: ");
  Serial.println(ldr);  

  if(digital_val==LOW)
    digital_val = HIGH;
  else
    digital_val = LOW; 

  delay(1000);
}
