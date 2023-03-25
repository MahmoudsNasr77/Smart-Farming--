#include <ESP8266WiFi.h>

#define trig D0
#define echo D1
#define flowPin D2
#define soilPin A0
#define led 2

//waterlevel
int waterLevel = 0;
int tankHeight = 50;

//soil moisture
int analogIn = 0;
const int dry = 816;
const int wet = 387;
int soilMoistureRead = 0;

//wifi&server Info
const char* ssid = "WE";
const char* password =  "M@e182001";
int PORT ;
const char * IP = "192.168.1.7";

//flow meter parameters
long currentMillis = 0;
long previousMillis = 0;
int interval = 1000;
float calibrationFactor = 4.5;
volatile byte pulseCount;
byte pulse1Sec = 0;
float flowRate;
float flowLitres;
float totalLitres;

WiFiClient client;

void connectingWifi(){
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
  delay(100);
  Serial.print(".");
  }
  Serial.print("WiFi connected with IP: ");
  Serial.println(WiFi.localIP());  
  Serial.print("mac address");
  Serial.println(WiFi.macAddress());
}

void IRAM_ATTR pulseCounter(){
  pulseCount++;
}
void setup(){ 
  Serial.begin(115200);
  connectingWifi();

  //check mac address then give ports
  if (WiFi.macAddress() == "4C:75:25:38:0B:CC"){
    PORT = 6000;
  }
  else if (WiFi.macAddress() =="A8:48:FA:FF:B9:EC"){
    PORT=6001;
  }
  else if (WiFi.macAddress() =="48:55:19:14:CA:DC"){
    PORT=6002;
  }
  else if (WiFi.macAddress() =="BC:FF:4D:CF:F5:48"){
    PORT=6003;
  } 
  
  pinMode(trig , OUTPUT);
  pinMode(echo , INPUT);
  pinMode(soilPin,INPUT);
  pinMode(flowPin, INPUT_PULLUP);
  pinMode(2,OUTPUT);
  pulseCount = 0;
  flowRate = 0.0;
  previousMillis = 0;
 
  attachInterrupt(digitalPinToInterrupt(flowPin), pulseCounter, FALLING);
}

void loop(){
  digitalWrite(led,LOW);
  client.connect(IP,PORT);
  if (client.connected()){
    flowMeter();
    waterLev();
    soilMoisture();
    client.write((String(waterLevel)+","+String(totalLitres)+","+String(soilMoistureRead)).c_str());
    Serial.println("Data was sent");
    client.flush();
    client.stop();
    digitalWrite(led,HIGH);
  }
  delay(1000);
}
void waterLev(){
  digitalWrite(trig, LOW);
  delayMicroseconds(5);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  int duration = pulseIn(echo, HIGH);
  int distance = duration /57;
  waterLevel = tankHeight - distance ;
}
void flowMeter(){
  currentMillis = millis();
  if (currentMillis - previousMillis > interval) 
  {
    
    pulse1Sec = pulseCount;
    pulseCount = 0;
    flowRate = ((1000.0 / (millis() - previousMillis)) * pulse1Sec) / calibrationFactor;
    previousMillis = millis();

    flowLitres = (flowRate / 60);
    totalLitres += flowLitres;
  }
}
void soilMoisture(){
  analogIn = analogRead(A0);
  soilMoistureRead = map(analogIn, wet, dry, 100, 0);
}