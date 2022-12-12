#include <WiFi.h>
#define trigger_pin 25
#define Echo_pin 27
#define trigger_pint 12
#define Echo_pint 14
#define LED 2

long duration;
int distance;
long durationt;
int distancet;
 
const char* ssid = "Replace your wifi name";
const char* password =  "*******";
 
const uint16_t port = 8090;
const char * host = "########";//ip address of the host machine

#define timeSeconds 1

// Set GPIOs for LED and PIR Motion Sensor
const int led = 19;
const int motionSensor = 5;

// Timer: Auxiliary variables
unsigned long now = millis();
unsigned long lastTrigger = 0;
boolean startTimer = false;
bool flagM = false;

// Checks if motion was detected, sets LED HIGH and starts a timer
void IRAM_ATTR detectsMovement() {
  //Serial.println("MOTION DETECTED!!!");
  flagM = true;
  digitalWrite(led, HIGH);
  startTimer = true;
  lastTrigger = millis();
}
 
void setup()
{
 
Serial.begin(9600);

/********************************** for PIR********************/
  // PIR Motion Sensor mode INPUT_PULLUP
  pinMode(motionSensor, INPUT_PULLUP);
  // Set motionSensor pin as interrupt, assign interrupt function and set RISING mode
  attachInterrupt(digitalPinToInterrupt(motionSensor), detectsMovement, RISING);

  // Set LED to LOW
  pinMode(led, OUTPUT);
  digitalWrite(led, LOW);
////////////////////////////////////////////////////////////////

pinMode(trigger_pin, OUTPUT); 
pinMode(LED, OUTPUT); 
pinMode(Echo_pin, INPUT); 

pinMode(trigger_pint, OUTPUT); // configure the trigger_pin(D9) as an Output

pinMode(Echo_pint, INPUT); // configure the Echo_pin(D11) as an Input
 
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("...");
  }
 
  Serial.print("WiFi connected with IP: ");
  Serial.println(WiFi.localIP());
 
}
 
void loop()
{

  // Current time
  now = millis();
  // Turn off the LED after the number of seconds defined in the timeSeconds variable
  if(startTimer && (now - lastTrigger > (timeSeconds*1000))) {
    Serial.println("Motion stopped...");
    //if want to set flagM to false uncomment the below line.
    //flagM = false;    
    digitalWrite(led, LOW);
    startTimer = false;
  }  

if(flagM)
{
  digitalWrite(trigger_pin, LOW); //set trigger signal low for 2us
  delayMicroseconds(2);


digitalWrite(trigger_pin, HIGH);  // make trigger pin active high
delayMicroseconds(10);            // wait for 10 microseconds
digitalWrite(trigger_pin, LOW);

duration = pulseIn(Echo_pin, HIGH); // save time duration value in "duration variable
distance= duration*0.034/2;

digitalWrite(trigger_pint, LOW); //set trigger signal low for 2us
delayMicroseconds(2);

digitalWrite(trigger_pint, HIGH);  // make trigger pin active high
delayMicroseconds(10);            // wait for 10 microseconds
digitalWrite(trigger_pint, LOW);   // make trigger pin active low


durationt = pulseIn(Echo_pint, HIGH); // save time duration value in "duration variable
distancet= durationt*0.034/2; //Convert pulse duration into distance
//if ( distance < 10)
//digitalWrite(LED, HIGH);
//else 
//digitalWrite(LED, LOW);
// print measured distance value on Arduino serial monitor
Serial.print("Distance1: ");
Serial.print(distance);
Serial.print("Distance2: ");
Serial.print(distancet);
//Serial.println(" cm");
    WiFiClient client;
 
    if (!client.connect(host, port)) {
 
        Serial.println("Connection to host failed");
        delay(1000);
        return;
    }
 
    Serial.println("Connected to server successful!");
 
    //client.print("Hello from ESP32!");
    client.print("distance1 ");
    client.print(distance);
     client.print("   distance2 ");
    client.print(distancet);
 
    Serial.println("Disconnecting...");
    client.stop();
  
    delay(5000);
}
}