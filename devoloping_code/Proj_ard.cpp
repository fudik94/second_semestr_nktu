#include <Servo.h>

#define pinServo 5
#define pinButt1 7
#define pinLED1 3
#define pinLED2 2
int buttonState = 0;
Servo myservo;

void setup() {
  myservo.attach(pinServo);
  
  pinMode(pinButt1, INPUT);
  pinMode(pinLED1, OUTPUT);
  pinMode(pinLED2, OUTPUT);
}

void loop()
{
  buttonState = digitalRead(pinButt1);
  if(digitalRead(pinButt1) == 0) myservo.write(0);
  if(digitalRead(pinButt1) == 1) myservo.write(180);
  
  if (buttonState == LOW){
    digitalWrite(pinLED1, HIGH);
    digitalWrite(pinLED2, LOW);
  }
  if (buttonState == HIGH) {
    digitalWrite(pinLED1, LOW);
    digitalWrite(pinLED2, HIGH);
  }

  delay(15);
}
