from system import youtubeOAuth


class SendChat:
    def __init__(self):
        auth = youtubeOAuth.get_oauth('readonly')
        request = auth.liveBroadcasts().list(
            part="snippet",
            broadcastStatus="active"
        )
        res = request.execute()
        self.liveChatId = res['items'][0]['snippet']['liveChatId']
        self.oauth = youtubeOAuth.get_oauth()

    def send(self, msg):
        request = self.oauth.liveChatMessages().insert(
            part="snippet",
            body={
                "snippet": {
                    "type": "textMessageEvent",
                    "liveChatId": self.liveChatId,
                    "textMessageDetails": {
                        "messageText": msg
                    }
                }
            }
        )
        response = request.execute()
        print(response)


if __name__ == '__main__':
    sendChat = SendChat()
    sendChat.send('# test')
