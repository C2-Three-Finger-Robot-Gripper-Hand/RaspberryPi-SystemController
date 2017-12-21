import minimalmodbus


class FingerController:
    def __init__(self, address):
        self.modbus = minimalmodbus.Instrument('/dev/serial0', address, minimalmodbus.MODE_ASCII)
        self.modbus.serial.baudrate = 115200
        self.modbus.serial.timeout = 0.2

    def calibrate(self):

        pass

    def set_motor_position(self, motor_number, degrees):
        if motor_number <= 3 and motor_number > 0:
            self.modbus.write_register(motor_number - 1, degrees)

