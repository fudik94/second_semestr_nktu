#include <LiquidCrystal.h>  // LCD library

// Ultrasonic sensor pins
#define TRIG1 7
#define ECHO1 6
#define TRIG2 10
#define ECHO2 9
#define TRIG3 A3
#define ECHO3 A2
#define TRIG4 A0
#define ECHO4 A1

#define BUZZER 8  // Buzzer pin

LiquidCrystal lcd(12, 11, 5, 4, 3, 2); // LCD pins

int cm1, cm2, cm3, cm4;

// Helper function to get distance from sensor
int getDistance(int trigPin, int echoPin) {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  int duration = pulseIn(echoPin, HIGH);
  return duration / 29 / 2;
}

// Display distance stage on LCD and beep
void showStage(int cm, int row, int col, const char* display, int delayTime) {
  if (cm > 0 && cm < 200) {
    lcd.setCursor(col, row);
    lcd.print(display);
    digitalWrite(BUZZER, HIGH);
    delay(delayTime);
    digitalWrite(BUZZER, LOW);
  } else {
    lcd.setCursor(col, row);
    lcd.print("  "); // clear display
    digitalWrite(BUZZER, LOW);
  }
}

void setup() {
  lcd.begin(16, 2);
  pinMode(BUZZER, OUTPUT);

  // Sensor pins
  pinMode(TRIG1, OUTPUT); pinMode(ECHO1, INPUT);
  pinMode(TRIG2, OUTPUT); pinMode(ECHO2, INPUT);
  pinMode(TRIG3, OUTPUT); pinMode(ECHO3, INPUT);
  pinMode(TRIG4, OUTPUT); pinMode(ECHO4, INPUT);

  Serial.begin(9600);
}

void loop() {
  // Read distances
  cm1 = getDistance(TRIG1, ECHO1);
  cm2 = getDistance(TRIG2, ECHO2);
  cm3 = getDistance(TRIG3, ECHO3);
  cm4 = getDistance(TRIG4, ECHO4);

  Serial.print("S1: "); Serial.println(cm1);
  Serial.print("S2: "); Serial.println(cm2);
  Serial.print("S3: "); Serial.println(cm3);
  Serial.print("S4: "); Serial.println(cm4);
  delay(200);

  // Display stages for each sensor
  // Sensor 1 (top right)
  if (cm1 > 150) showStage(cm1, 0, 14, "--", 1000);
  else if (cm1 > 100) showStage(cm1, 0, 12, "==--", 500);
  else if (cm1 > 50) showStage(cm1, 0, 10, "%%==--", 100);
  else if (cm1 > 0) showStage(cm1, 0, 8, "&&%%==--", 5);

  // Sensor 2 (top left)
  if (cm2 > 150) showStage(cm2, 0, 0, "--", 1000);
  else if (cm2 > 100) showStage(cm2, 0, 0, "--==", 500);
  else if (cm2 > 50) showStage(cm2, 0, 0, "--==##", 100);
  else if (cm2 > 0) showStage(cm2, 0, 0, "--==##**", 5);

  // Sensor 3 (bottom right)
  if (cm3 > 150) showStage(cm3, 1, 14, "--", 1000);
  else if (cm3 > 100) showStage(cm3, 1, 12, "==--", 500);
  else if (cm3 > 50) showStage(cm3, 1, 10, "%%==--", 100);
  else if (cm3 > 0) showStage(cm3, 1, 8, "&&%%==--", 5);

  // Sensor 4 (bottom left)
  if (cm4 > 150) showStage(cm4, 1, 0, "--", 1000);
  else if (cm4 > 100) showStage(cm4, 1, 0, "--==", 500);
  else if (cm4 > 50) showStage(cm4, 1, 0, "--==##", 100);
  else if (cm4 > 0) showStage(cm4, 1, 0, "--==##**", 5);
}
