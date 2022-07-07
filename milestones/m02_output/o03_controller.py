from system import sendSerial


class Controller:
    def __init__(self):
        self.sendSerial = sendSerial.SendSerial()

    def press_key(self, text):
        self.sendSerial.press_key(text)


if __name__ == '__main__':
    controller = Controller()
    controller.press_key('a')
