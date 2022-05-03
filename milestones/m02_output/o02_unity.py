import websocket
import settings
UNITY_PORT = settings.UNITY_PORT
url_unity = f'ws://localhost:{UNITY_PORT}'


def send(msg):
    ws = websocket.create_connection(url_unity)
    ws.send(msg)
    ws.close()


if __name__ == '__main__':
    send('speak 1')
