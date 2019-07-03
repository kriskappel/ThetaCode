#include <ros.h>
#include <std_msgs/Int16.h>
#include <std_msgs/Bool.h>

#define odometryPinRight 2
#define odometryPinLeft 3

unsigned int right_counter = 0;
unsigned int left_counter = 0;
unsigned int sensor_counter_right = 0;
unsigned int sensor_counter_left = 0;
unsigned int pulses_final = 0;

bool right = false;
bool left = false;


void clearCounter(const std_msgs::Bool &shouldClear)
{
  if (shouldClear.data)
  {
    right_counter = 0;
    left_counter = 0;
  }
}

void numPulses(const std_msgs::Int16 &npulses) 
{ 
  left_counter  = 0;
  right_counter = 0;

  right = false;
  left = false;

  pulses_final = npulses;
}

ros::NodeHandle node;
std_msgs::Int16 value_odometry_right;
std_msgs::Int16 value_odometry_left;
ros::Publisher odometry_pub_right("right_sensor", &value_odometry_right);
ros::Publisher odometry_pub_left("left_sensor", &value_odometry_left);
ros::Subscriber<std_msgs::Bool> clear_counter("pattern", &clearCounter);
ros::Subscriber<std_msgs::Int16> num_pulses("pulses", &numPulses);

void setup()
{
  Serial.begin(9600);
  pinMode(odometryPinRight, INPUT);
  pinMode(odometryPinLeft, INPUT);
  node.initNode();
  node.advertise(odometry_pub_right);
  node.advertise(odometry_pub_left);
  node.subscribe(clear_counter);
  node.subscribe(num_pulses);
  attachInterrupt(digitalPinToInterrupt(odometryPinRight), counterRight, RISING);
  attachInterrupt(digitalPinToInterrupt(odometryPinLeft), counterLeft, RISING);
}


void loop()
{
  if (right_counter >= pulses_final and !right)
  {
    value_odometry_right.data = right_counter;
    odometry_pub_right.publish(&value_odometry_right);
    right = !right;
  }
  if (left_counter >= pulses_final and !left)
  {
    value_odometry_left.data = left_counter;
    odometry_pub_left.publish(&value_odometry_left);
    left = !left;
  }
  node.spinOnce();
}


void counterRight()
{
  right_counter++;
}

void counterLeft()
{
  sensor_counter_left++;
}
