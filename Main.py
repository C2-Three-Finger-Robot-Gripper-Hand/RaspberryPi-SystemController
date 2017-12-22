import FingerController
import RosCommunicator


class GripperHand:
    def __init__(self):
        self.finger1_controller = FingerController.FingerController(1)
        self.finger2_controller = FingerController.FingerController(2)
        self.finger3_controller = FingerController.FingerController(3)

        self.ros_comunicator = RosCommunicator.RosCommunicator(self.finger1_controller,
                                                               self.finger2_controller,
                                                               self.finger3_controller)

if __name__ == "__main__":
    GripperHand()
