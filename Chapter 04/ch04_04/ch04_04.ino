#include <SoftwareSerial.h>
#include <TinyGPS.h>

// D2   >>>  Rx, D4   >>>  Tx
SoftwareSerial bluetooth(2, 4); // RX, TX

// D5   >>>  Rx, D11   >>>  Tx
SoftwareSerial gps(5, 11);  // RX, TX
char val;
TinyGPS gps_mod;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);  
  bluetooth.begin(9600);  
  Serial.println("Bluetooth On..");
  gps.begin(9600);  
  Serial.println("GPS On..");
}

void loop() {
  bool newData = false;
  unsigned long chars;
  unsigned short sentences, failed;

  // read GPS position every 3 seconds
  for (unsigned long start = millis(); millis() - start < 3000;) {
    while (gps.available()){
      char c = gps.read();  
      //Serial.println(c);    
      if (gps_mod.encode(c)) 
        newData = true;
    }
  }

  if (newData) {
    float flat, flon;
    unsigned long age;

    digitalWrite(13, HIGH);
    gps_mod.f_get_position(&flat, &flon, &age);
    print_data("LAT=");
    print_num_data(flat == TinyGPS::GPS_INVALID_F_ANGLE ? 0.0 : flat, 6);
    print_data(" LON=");
    print_num_data(flon == TinyGPS::GPS_INVALID_F_ANGLE ? 0.0 : flon, 6);
    print_data(" SAT=");
    print_num_data(gps_mod.satellites() == TinyGPS::GPS_INVALID_SATELLITES ? 0 : gps_mod.satellites());
    print_data(" PREC=");
    print_num_data(gps_mod.hdop() == TinyGPS::GPS_INVALID_HDOP ? 0 : gps_mod.hdop());

    break_line();
    digitalWrite(13, LOW);
  }      
}

void print_data(char msg[30]) {
  Serial.print(msg);
  bluetooth.print(msg);
}
void print_num_data(float msg,int n) {
  Serial.print(msg, n);
  bluetooth.print(msg, n);
}
void print_num_data(int msg) {
  Serial.print(msg);
  bluetooth.print(msg);
}
void break_line() {
  Serial.println("");
  bluetooth.println("");
}



