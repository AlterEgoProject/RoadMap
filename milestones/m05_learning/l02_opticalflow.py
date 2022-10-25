import cv2
import numpy as np
import matplotlib.pyplot as plt


class OpticaFlow:
    def __init__(self, frame=None):
        self.prevgray = None
        if frame is not None:
            self.set(frame)

    def set(self, frame):
        img = cv2.resize(frame, (300, 300))
        self.prevgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def update(self, frame):
        img = cv2.resize(frame, (300, 300))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        flow = cv2.calcOpticalFlowFarneback(self.prevgray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        self.prevgray = gray
        cv2.imshow('flow', draw_flow(img, flow, 8))


def draw_flow(img, flow, step=16):
    h, w = img.shape[:2]
    y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1).astype(int)
    fx, fy = flow[y,x].T
    lines = np.vstack([x, y, x+fx, y+fy]).T.reshape(-1, 2, 2)
    lines = np.int32(lines + 0.5)
    if len(img.shape) == 2:
        vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    else:
        vis = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.polylines(vis, lines, 0, (0, 255, 0))
    return vis


if __name__ == '__main__':
    from milestones.m01_input.i02_display import Display
    from time import sleep
    display = Display()
    opt = OpticaFlow(display.get_snap())
    sleep(1)
    while(1):
        opt.update(display.get_snap())
        ch = cv2.waitKey(5)
        if ch == 27:
            break