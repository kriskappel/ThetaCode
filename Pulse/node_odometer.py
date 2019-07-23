#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Bool
from std_msgs.msg import String

leftValue = 0
rightValue = 0
state = 'firstStop'
flag_stop = False

def turnRight():
    try:
        startMovimentTurnRight()
    except rospy.ROSInnterruptException:
        pass

def turnLeft():
    try:
        startMovimentTurnLeft()
    except rospy.ROSInnterruptException:
        pass

def goAhead():
    try:
        startMovimentAhead()
    except rospy.ROSInnterruptException:
        pass

# def followMe():
#     try:
#         None
#     except rospy.ROSInnterruptException:
#         pass

def stopMoviment():
    #print "stop move"
    try:
        stop()
    except rospy.ROSInnterruptException:
        pass

def callbackLeft(data):
    #print "cbleft"
    global leftValue
    leftValue = int(data.data)
    evaluateStop()

def callbackRight(data):
    #print "cbright"
    global rightValue
    rightValue = int(data.data)
    evaluateStop()

def callbackWalk(data):
    global state
    if data.data == 'go ahead':
        print 'GO AHEAD'
        state = 'goAhead'
        goAhead()
        print 'END GO AHEAD'
    elif data.data == 'turn left':
        state = 'turnLeft'
        turnLeft()
    elif data.data == 'turn right':
        state = 'turnRight'
        turnRight()
    elif data.data == 'follow me':
        print('followMe')
        state = 'followMe'
        None
    elif data.data == 'stop':
        state = 'stop'
        stopMoviment()

def stopGoAhead(value, distance):
    #print "stop go ahead"
    #print value
    #print (value/300.0)*3.14*0.34 >= distance
    return (value/300.0)*3.14*0.34 >= distance

def evaluateStop():
    #print "evaluate stop"
    global state
    global leftValue
    global rightValue

    if state == 'firstStop':
        state = ''
        stopMoviment()
    if state == 'turnRight' and leftValue >= 100 and rightValue >= 100:
        print "TURN RIGHT : left value " + str(leftValue) + " right value " + str(rightValue)
        stopMoviment()
    elif state == 'turnLeft' and rightValue >= 100 and leftValue >= 100:
        print "TURN LEFT : left value " + str(leftValue) + " right value " + str(rightValue)
        stopMoviment()
    elif state == 'goAhead' and (stopGoAhead(rightValue, 1.0) or stopGoAhead(leftValue, 1.0)):
        print "###RIGHT VALUE:" + str(rightValue) + "\n###LEFT VALUE:" + str(leftValue)
        stopMoviment()
    elif state == 'followMe':
        None
    elif state == 'stop':
        stopMoviment()

def startMovimentTurnRight():
    #print "start right"
    pub = rospy.Publisher('pattern', Bool, queue_size = 1000)
    pub.publish(True)
    move = rospy.Publisher('channel_x', Int16, queue_size = 1000)
    move.publish(95)

def startMovimentTurnLeft():
    #print "start left"
    pub = rospy.Publisher('pattern', Bool, queue_size = 1000)
    pub.publish(True)
    move = rospy.Publisher('channel_x', Int16, queue_size = 1000)
    move.publish(170)

def startMovimentAhead():
    #print "start ahead"
    pub = rospy.Publisher('pattern', Bool, queue_size = 1000)
    pub.publish(True)
    move = rospy.Publisher('channel_y', Int16, queue_size = 1000)
    move.publish(175)
    print("175 publicado")

def stop():
    print "stop"
    pub = rospy.Publisher('pattern', Bool, queue_size = 1000)
    pub.publish(True)
    stopy = rospy.Publisher('channel_y', Int16, queue_size = 1000)
    stopy.publish(135)
    stopx = rospy.Publisher('channel_x', Int16, queue_size = 1000)
    stopx.publish(135)

# def first_stop():
#     pub = rospy.Publisher('walk', String, queue_size = 100)
#     pub.publish("stop")
#     print "oi"

def listener():
    #print "listener"
    global flag_stop
    rospy.Subscriber("left_sensor", Int16, callbackLeft)
    rospy.Subscriber("right_sensor", Int16, callbackRight)
    rospy.Subscriber("walk", String, callbackWalk)
    rospy.spin()

if __name__ == '__main__':
    #print "main"
    rospy.init_node('node_odometer', anonymous=True)
    listener()
