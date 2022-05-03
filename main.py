from system import youtubeStream


def main():
    # 配信の制御
    streaming = youtubeStream.Streaming()
    while True:
        streaming.update_page()
    print()


if __name__ == '__main__':
    main()
