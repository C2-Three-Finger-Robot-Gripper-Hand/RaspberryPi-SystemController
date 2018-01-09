import rospy
from std_msgs.msg import Int16
import FingerController

class RosCommunicator:
    def __init__(self, finger1, finger2, finger3):
        rospy.init_node('gripperhand', anonymous=True)
        self.finger1_controller = finger1
        self.finger2_controller = finger2
        self.finger3_controller = finger3

        self.finger1_motor1_value = rospy.Publisher("finger1_motor1_value", Int16, queue_size=10)
        self.finger1_motor2_value = rospy.Publisher("finger1_motor2_value", Int16, queue_size=10)
        self.finger1_motor3_value = rospy.Publisher("finger1_motor3_value", Int16, queue_size=10)
        self.finger2_motor1_value = rospy.Publisher("finger2_motor1_value", Int16, queue_size=10)
        self.finger2_motor2_value = rospy.Publisher("finger2_motor2_value", Int16, queue_size=10)
        self.finger2_motor3_value = rospy.Publisher("finger2_motor3_value", Int16, queue_size=10)
        self.finger3_motor1_value = rospy.Publisher("finger3_motor1_value", Int16, queue_size=10)
        self.finger3_motor2_value = rospy.Publisher("finger3_motor2_value", Int16, queue_size=10)
        self.finger3_motor3_value = rospy.Publisher("finger3_motor3_value", Int16, queue_size=10)

        rospy.Subscriber('finger1_motor1_set', Int16, self.finger1_motor1_set)
        rospy.Subscriber('finger1_motor2_set', Int16, self.finger1_motor2_set)
        rospy.Subscriber('finger1_motor3_set', Int16, self.finger1_motor3_set)
        rospy.Subscriber('finger2_motor1_set', Int16, self.finger2_motor1_set)
        rospy.Subscriber('finger2_motor2_set', Int16, self.finger2_motor2_set)
        rospy.Subscriber('finger2_motor3_set', Int16, self.finger2_motor3_set)
        rospy.Subscriber('finger3_motor1_set', Int16, self.finger3_motor1_set)
        rospy.Subscriber('finger3_motor2_set', Int16, self.finger3_motor2_set)
        rospy.Subscriber('finger3_motor3_set', Int16, self.finger3_motor3_set)

        rospy.Subscriber('finger1_calibrate', Int16, self.finger1_controller.calibrate)

    #
    # set functions
    #
    def finger1_motor1_set(self, value):
        self.finger1_controller.set_motor_position(1, value.data)

    def finger1_motor2_set(self, value):
        self.finger1_controller.set_motor_position(2, value.data)

    def finger1_motor3_set(self, value):
        self.finger1_controller.set_motor_position(3, value.data)

    def finger2_motor1_set(self, value):
        self.finger2_controller.set_motor_position(1, value.data)

    def finger2_motor2_set(self, value):
        self.finger2_controller.set_motor_position(2, value.data)

    def finger2_motor3_set(self, value):
        self.finger2_controller.set_motor_position(3, value.data)

    def finger3_motor1_set(self, value):
        self.finger3_controller.set_motor_position(1, value.data)

    def finger3_motor2_set(self, value):
        self.finger3_controller.set_motor_position(2, value.data)

    def finger3_motor3_set(self, value):
        self.finger3_controller.set_motor_position(3, value.data)

    def publish_sensors(self):
        self.finger1_motor1_value.publish(self.finger1_controller.motor1_value)
        self.finger1_motor2_value.publish(self.finger1_controller.motor2_value)
        self.finger1_motor3_value.publish(self.finger1_controller.motor3_value)
        self.finger2_motor1_value.publish(self.finger2_controller.motor1_value)
        self.finger2_motor2_value.publish(self.finger2_controller.motor2_value)
        self.finger2_motor3_value.publish(self.finger2_controller.motor3_value)
        self.finger3_motor1_value.publish(self.finger3_controller.motor1_value)
        self.finger3_motor2_value.publish(self.finger3_controller.motor2_value)
        self.finger3_motor3_value.publish(self.finger3_controller.motor3_value)

