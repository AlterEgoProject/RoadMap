import matplotlib.pyplot as plt
import numpy as np


class FinderLayer:
    def __init__(self, display):
        self.display = display
        # 学習レイヤー読み込み
        # オプティカルフローのセット
        # 3色+グレースケール の学習平面
        pass

    def update(self):
        plt.clf()
        plt.imshow(self.display.get_snap())
        plt.pause(0.1)
        pass


if __name__ == '__main__':
    from milestones.m01_input.i02_display import Display
    display = Display()
    fl = FinderLayer(display)
    for _ in range(100):
        fl.update()
