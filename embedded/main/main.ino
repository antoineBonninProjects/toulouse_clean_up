#include <SigFox.h>


uint16_t temp = 0xA0B1;
uint8_t bitfield = 0b101;

#define DEBUG 0

void setup() {

  if (DEBUG){
    Serial.begin(9600);
    while (!Serial) {};
  }

  // Initialize the SigFox module
  if (!SigFox.begin()) {
    if (DEBUG){
      Serial.println("Sigfox module unavailable !");
    }
    return;
  }

  // If we wanto to debug the application, print the device ID to easily find it in the backend
  if (DEBUG){
    SigFox.debug();
    Serial.println("ID  = " + SigFox.ID());
  }

  delay(100);

  // Compose a message as usual; the single bit transmission will be performed transparently
  // if the data we want to send is suitable
  SigFox.beginPacket();
  
  SigFox.write(temp);
  SigFox.write(bitfield);

  int ret = SigFox.endPacket();

  if (DEBUG){
    Serial.print("Status : ");
    Serial.println(ret);
  }
}

void loop(){}
