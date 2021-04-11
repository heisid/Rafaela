#include <SoftwareSerial.h>
#include <SerialCommand.h>
#include <AFMotor.h>
#include <PWMServo.h>
#include <NewPing.h>
#include <MPU6050_tockn.h>
#include <Wire.h>

#define BT_RX A0
#define BT_TX A1
#define TRIG 9
#define ECHO A3
#define BUFFER_SIZE 8
#define BT_SPEED 9600
#define SERVO_PIN 10
#define RIGHT 2
#define LEFT 1

SoftwareSerial bluetooth(BT_RX, BT_TX);
SerialCommand cmd(bluetooth);
AF_DCMotor right_motor(RIGHT);
AF_DCMotor left_motor(LEFT);
PWMServo servo;
NewPing sonar(TRIG, ECHO);
MPU6050 accel(Wire);

void move(AF_DCMotor &motor, int speed) {
  motor.setSpeed(abs(speed));
  if (speed > 0) {
    motor.run(FORWARD);
  } else if (speed < 0) {
    motor.run(BACKWARD);
  } else motor.run(RELEASE);
}

void move_right_motor() {
  char *arg = cmd.next();
  int speed = atoi(arg);
  move(right_motor, speed);
}

void move_left_motor() {
  char *arg = cmd.next();
  int speed = atoi(arg);
  move(left_motor, speed);
}

void move_servo() {
  char *arg = cmd.next();
  int angle = map(atoi(arg), -90, 90, 0, 180);
  servo.write(angle);
}

void request_sonar() {
  bluetooth.println(sonar.ping_cm());
}

void request_accel() {
  accel.update();
  bluetooth.print(accel.getAccX());
  bluetooth.print(",");
  bluetooth.print(accel.getAccY());
  bluetooth.print(",");
  bluetooth.print(accel.getAccZ());
  bluetooth.print(",");
  bluetooth.print(accel.getAngleX());
  bluetooth.print(",");
  bluetooth.print(accel.getAngleY());
  bluetooth.print(",");
  bluetooth.print(accel.getAngleZ());
  bluetooth.print(",");
  request_uptime();
  delay(50);
}

void request_uptime() {
  bluetooth.println(millis());
}

void setup() {
  servo.attach(SERVO_PIN);
  bluetooth.begin(BT_SPEED);
  Wire.begin();
  accel.begin();
  accel.calcGyroOffsets(true);
  cmd.addCommand("l", move_left_motor);
  cmd.addCommand("r", move_right_motor);
  cmd.addCommand("s", move_servo);
  cmd.addCommand("p", request_sonar);
  cmd.addCommand("a", request_accel);
  cmd.addCommand("t", request_uptime);
}

void loop() {
  cmd.readSerial();
}
