
import rospy
from tf2_msgs.msg import TFMessage

from std_msgs.msg import Int16

def callback(data):
	#print data
	if "torso" in data.transforms[0].child_frame_id:
		tx = data.transforms[0].transform.translation.x
		ty = data.transforms[0].transform.translation.y
		ex = ty
		ey = tx - 2.0

		
		cmd_x = 0
		cmd_y = 0

		if ex < 0 and ey < 0:
			cmd_x = 135
			cmd_y = 100 + 1 * ey

		elif ex >= 0 and ey >= 0:
			cmd_x = 170 + 1 * ex
			cmd_y = 170 + 1 * ey

		elif ex < 0 and ey >= 0:
			cmd_x = 135
			cmd_y = 170 + 1 * ey

		elif ex >= 0 and ey < 0:
			cmd_x = 170 + 1 * ex
			cmd_y = 100 + 1 * ey
		
		
		print "cmd_x " + str(cmd_x) 
		print "cmd_y " + str(cmd_y)

		pub = rospy.Publisher('channel_x', Int16, queue_size=10)
		pub.publish(cmd_x)
		pub = rospy.Publisher('channel_y', Int16, queue_size=10)
		pub.publish(cmd_y)


def listener():
	rospy.init_node('filter', anonymous=True)

	rospy.Subscriber("tf", TFMessage, callback)


	rospy.spin()

if __name__ == '__main__':
	#v1 = 0
	#v2 = 0
	listener()