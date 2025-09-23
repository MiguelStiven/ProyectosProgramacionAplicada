#include <Arduino.h>

void setup() {
  pinMode(2, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(18, OUTPUT);
  pinMode(19, OUTPUT);
  pinMode(21, OUTPUT);
  pinMode(22, OUTPUT);
  pinMode(23, OUTPUT);
  pinMode(25, OUTPUT);
}

void loop() {
  digitalWrite(2, HIGH);
  delay(1000);
  digitalWrite(2, LOW);

  digitalWrite(5, HIGH);
  delay(1000);
  digitalWrite(5, LOW);

  digitalWrite(18, HIGH);
  delay(1000);
  digitalWrite(18, LOW);

  digitalWrite(19, HIGH);
  delay(1000);
  digitalWrite(19, LOW);

  digitalWrite(21, HIGH);
  delay(1000);
  digitalWrite(21, LOW);

  digitalWrite(22, HIGH);
  delay(1000);
  digitalWrite(22, LOW);

  digitalWrite(23, HIGH);
  delay(1000);
  digitalWrite(23, LOW);

  digitalWrite(25, HIGH);
  delay(1000);
  digitalWrite(25, LOW);
}
