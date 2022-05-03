ZEN = "".join(chr(0xff01 + i) for i in range(94))
HAN = "".join(chr(0x21 + i) for i in range(94))
ZEN2HAN = str.maketrans(ZEN, HAN)


def translate(text):
    return text.translate(ZEN2HAN)


if __name__ == '__main__':
    print(translate('テスト・１・/'))
