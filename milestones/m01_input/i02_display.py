import cv2
import numpy as np
from system import obsControl

class Display:
    def __init__(self):
        self.cam = cv2.VideoCapture(1)
        self.cam.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT,  1080)
        obs = obsControl.ObsControl()
        info = obs.aver_info
        aver_shape = info.getWidth(), info.getHeight()
        pos = info.getPosition()
        aver_pos = pos['x'], pos['y']
        crop_pos = [int(aver_pos[i]) for i in range(2)]
        crop_len = [int(aver_shape[i]) for i in range(2)]
        self.crop_y = (crop_pos[1] + 1, crop_pos[1] + crop_len[1] - 1)
        self.crop_x = (crop_pos[0] + 1, crop_pos[0] + crop_len[0] - 1)

    def read(self):
        self.cam.read()
        ret, frame = self.cam.read()
        if not ret:
            return np.zeros((1080, 1920, 3))
        frame = frame[self.crop_y[0]:self.crop_y[1], self.crop_x[0]:self.crop_x[1]]  # 不要な部分を除去
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (1920, 1080))
        return frame


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    display = Display()
    display.read()
