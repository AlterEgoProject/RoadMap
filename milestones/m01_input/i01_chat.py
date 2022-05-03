import requests
import re
import settings
channel_id = settings.CHANNEL_ID


class GetChat:
    def __init__(self):
        load_url = f'https://www.youtube.com/channel/{channel_id}/live'
        html = requests.get(load_url)
        match_key = re.search(r'innertubeApiKey":".*?"', html.content.decode())
        apikey = match_key.group().split('"')[2]
        self.url = f'https://www.youtube.com/youtubei/v1/live_chat/get_live_chat?key={apikey}'
        match_key = re.search(r'continuation":".*?"', html.content.decode())
        self.continuation = match_key.group().split('"')[2]

    def get(self):
        res = self.send_post()
        chats = self.parse_response(res)
        return chats

    def send_post(self):
        body = {
            'context': {
                'client': {
                    'clientName': 'WEB',
                    'clientVersion': '2.20210126.08.02',
                    'timeZone': 'Asia/Tokyo',
                    'utcOffsetMinutes': 540,
                    'mainAppWebInfo': {
                        'graftUrl': 'https://www.youtube.com/live_chat?continuation=',
                    },
                },
                'request': {
                    'useSsl': True,
                },
            },
            'continuation': self.continuation,
        }
        response = requests.post(self.url, json=body)
        return response

    def parse_response(self, response):
        data = response.json()
        temp = data['continuationContents']['liveChatContinuation']
        # 公式チャンネルは timedContinuationData?
        self.continuation = temp['continuations'][0]['invalidationContinuationData']['continuation']
        chats = []
        for action in temp.get('actions', []):
            if 'liveChatTextMessageRenderer' not in action['addChatItemAction']['item'].keys():
                continue
            temp_a = action['addChatItemAction']['item']['liveChatTextMessageRenderer']
            chats.append({
                'text': temp_a['message']['runs'][0]['text'],
                'name': temp_a['authorName']['simpleText'],
                'channel': temp_a['authorExternalChannelId'],
                'id': temp_a['id'],
                'timestamp': temp_a['timestampUsec'],
                'isOwner': 'authorBadges' in temp_a.keys(),
            })
        return chats


if __name__ == '__main__':
    from time import sleep
    getChat = GetChat()
    for _ in range(1000):
        sleep(1)
        [print(chat['text']) for chat in getChat.get()]
