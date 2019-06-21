#include <ros.h>
#include <std_msgs/Int16.h>

#define pwmPinY 5
#define pwmPinX 6
#define stopped 135

void getDirectionFromTopicX(const std_msgs::Int16 &pwm)
{
  moveX(pwm.data);
}

void getDirectionFromTopicY(const std_msgs::Int16 &pwm)
{
  moveY(pwm.data);
}

ros::NodeHandle node;
ros::Subscriber<std_msgs::Int16> movement_x("channel_x", &getDirectionFromTopicX);
ros::Subscriber<std_msgs::Int16> movement_y("channel_y", &getDirectionFromTopicY);

void setup()
{
  Serial.begin(9600);
  pinMode(pwmPinY, OUTPUT);
  pinMode(pwmPinX, OUTPUT);
  analogWrite(pwmPinY, stopped);
  analogWrite(pwmPinX, stopped);
  node.initNode();
  node.subscribe(movement_x);
  node.subscribe(movement_y);
}

void loop()
{
  node.spinOnce();
}

void moveX(int pwm)
{
  analogWrite(pwmPinX, pwm);
}

void moveY(int pwm)
{
  analogWrite(pwmPinY, pwm);
}
