import minimalmodbus


class FingerController:
    def __init__(self, address):
        self.modbus = minimalmodbus.Instrument('/dev/serial0', address, minimalmodbus.MODE_ASCII)
        self.modbus.precalculate_read_size = False

        self.modbus.serial.baudrate = 115200
        self.modbus.serial.timeout = 0.05

        self.motor1_value = 0
        self.motor2_value = 0
        self.motor3_value = 0

    def calibrate(self, value):
	self.modbus.write_register(3, 2)
        pass

    def set_motor_position(self, motor_number, degrees):
        if motor_number <= 3 and motor_number > 0:
            try:
                self.modbus.write_register(motor_number - 1, degrees)
            except Exception as e:
                print("Error while setting motor position: ", e)

    def poll_sensors(self):
        try:
            self.motor1_value = self.modbus.read_register(0, 0)
            self.motor2_value = self.modbus.read_register(1, 0)
            self.motor3_value = self.modbus.read_register(2, 0)
        except Exception as e:
            print("Error while reading modbus: ", e)
