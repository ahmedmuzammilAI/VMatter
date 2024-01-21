///* Create a WiFi access point and provide a web server on it esp8266. */
//// For more details see http://42bots.com.
//*/

#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

IPAddress    apIP(42, 42, 42, 42);  // Defining a static IP address: local & gateway
                                    // Default IP in AP mode is 192.168.4.1

/* This are the WiFi access point settings. Update them to your likin */
const char *ssid = "realme X7 5G";
const char *password = "Rayan123";

// Define a web server at port 80 for HTTP
ESP8266WebServer server(80);

const int ledPin = 1; // an LED is connected to NodeMCU pin D1 (ESP8266 GPIO5) via a 1K Ohm resistor

bool ledState = false;
int generateRandomBPSystolic() {
  return random(100, 160);  // Adjust range as needed
}

int generateRandomBPDiastolic() {
  return random(60, 90);  // Adjust range as needed
}

int generateRandomHeartRate() {
  return random(60, 100);  // Adjust range as needed
}

float generateRandomTemperature() {
  return random(35.5, 37.5);  // Adjust range as needed
}

int generateRandomSpO2() {
  return random(95, 100);  // Adjust range as needed
}
void handleRoot() {
  digitalWrite (LED_BUILTIN, 0); //turn the built in LED on pin DO of NodeMCU on
  digitalWrite (ledPin, server.arg("led").toInt());
  ledState = digitalRead(ledPin);
    int systolicBP = generateRandomBPSystolic();
    int diastolicBP = generateRandomBPDiastolic();
    int heartRate = generateRandomHeartRate();
    float temperature = generateRandomTemperature();
    int spo2 = generateRandomSpO2();
 /* Dynamically generate the LED toggle link, based on its current state (on or off)*/
  char ledText[80];
  
  if (ledState) {
    strcpy(ledText, "LED is on. <a href=\"/?led=0\">Turn it OFF!</a>");
  }

  else {
    strcpy(ledText, "LED is OFF. <a href=\"/?led=1\">Turn it ON!</a>");
  }
 
  ledState = digitalRead(ledPin);

  char html[1000];
  int sec = millis() / 1000;
  int min = sec / 60;
  int hr = min / 60;

  int brightness = analogRead(A0);
  brightness = (int)(brightness + 5) / 10; //converting the 0-1024 value to a (approximately) percentage value

// Build an HTML page to display on the web-server root address
  
snprintf(html, 1000,
    "<html>\
      <head>\
        <meta http-equiv='refresh' content='10'/>\
        <title>Health Sensor Data from ESP</title>\
      </head>\
      <body>\
        <h1>Health Sensor Data Published from ESP</h1>\
        <p>Blood Pressure: %d/%d mmHg</p>\
        <p>Heart Rate: %d bpm</p>\
        <p>Temperature: %.1f °C</p>\
        <p>SpO2: %d%</p>\
        </body>\
    </html>",
    hr, min % 60, sec % 60, brightness, ledText, systolicBP, diastolicBP, heartRate, temperature, spo2
  );
  server.send ( 200, "text/html", html );
  digitalWrite ( LED_BUILTIN, 1 );
}

void handleNotFound() {
  digitalWrite ( LED_BUILTIN, 0 );
  String message = "File Not Found\n\n";
  message += "URI: ";
  message += server.uri();
  message += "\nMethod: ";
  message += ( server.method() == HTTP_GET ) ? "GET" : "POST";
  message += "\nArguments: ";
  message += server.args();
  message += "\n";

  for ( uint8_t i = 0; i < server.args(); i++ ) {
    message += " " + server.argName ( i ) + ": " + server.arg ( i ) + "\n";
  }

  server.send ( 404, "text/plain", message );
  digitalWrite ( LED_BUILTIN, 1 ); //turn the built in LED on pin DO of NodeMCU off
}

void setup() {
  pinMode ( ledPin, OUTPUT );
  digitalWrite ( ledPin, 0 );
  
  delay(1000);
  Serial.begin(115200);
  Serial.println();
  Serial.println("Configuring access point...");

  //set-up the custom IP address
  WiFi.mode(WIFI_AP_STA);
  WiFi.softAPConfig(apIP, apIP, IPAddress(255, 255, 255, 0));   // subnet FF FF FF 00  
  
  /* You can remove the password parameter if you want the AP to be open. */
  WiFi.softAP(ssid, password);

  IPAddress myIP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(myIP);
 
  server.on ( "/", handleRoot );
  server.on ( "/led=1", handleRoot);
  server.on ( "/led=0", handleRoot);
  server.on ( "/inline", []() {
    server.send ( 200, "text/plain", "this works as well" );
  } );
  server.onNotFound ( handleNotFound );
  
  server.begin();
  Serial.println("HTTP server started");
}

void loop() {
  server.handleClient();
}
