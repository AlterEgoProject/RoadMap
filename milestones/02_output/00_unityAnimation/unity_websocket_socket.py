from pytool.websocket_client import Websocket_Client
from dotenv import load_dotenv
import os
load_dotenv(override=True)
UNITY_PORT = os.getenv('UNITY_WEBSOCKET_PORT')


class UnityWebsocketClient(Websocket_Client):
    def __init__(self):
        super(UnityWebsocketClient, self).__init__(f'ws://localhost:{UNITY_PORT}')
        self.run_forever()

    def on_message(self, ws, message):
        print("on_message : {}".format(message))

    def run(self, *args):
        pass
        # while True:
        #     input_data = input("send data:")
        #     self.ws.send(input_data)
        # result = self.ws.recv()
        # print("run return '%s'" % result)


if __name__ == '__main__':
    uw = UnityWebsocketClient()
    print()
