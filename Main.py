import FingerController
import RosCommunicator
import time

class GripperHand:
    def __init__(self):
        self.finger1_controller = FingerController.FingerController(1)
        self.finger2_controller = FingerController.FingerController(2)
        self.finger3_controller = FingerController.FingerController(3)

        self.ros_communicator = RosCommunicator.RosCommunicator(self.finger1_controller,
                                                               self.finger2_controller,
                                                               self.finger3_controller)

    def poll_sensors(self):
        self.finger1_controller.poll_sensors()
        #self.finger2_controller.poll_sensors()
        #self.finger3_controller.poll_sensors()

if __name__ == "__main__":
    gripperhand = GripperHand()
    while(1):
        try:
            gripperhand.poll_sensors()
            gripperhand.ros_communicator.publish_sensors()
            time.sleep(0.1)
        except KeyboardInterrupt:
            print("Exiting..")
            break



