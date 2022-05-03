import numpy as np
import pyaudio
from scipy import fftpack
from scipy.signal import lfilter


class AudioInput():
    def __init__(self, chunk=1024):
        self.CHUNK = chunk
        self.RATE = 44100
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=pyaudio.paInt16,
                                    channels=1,
                                    rate=self.RATE,
                                    input=True,
                                    input_device_index=2,
                                    frames_per_buffer=self.CHUNK)
        self.freqList = fftpack.fftfreq(self.CHUNK, d=1.0 / self.RATE)[:self.CHUNK // 2]
        self.hamming = np.hamming(self.CHUNK)

    def sec2chunkn(self, sec):
        return int(sec * self.RATE // self.CHUNK)

    def get_input(self):
        binary_ret = self.stream.read(self.CHUNK)
        return binary_ret

    def get_float(self):
        ret = np.frombuffer(self.get_input(), dtype="int16") / 32768
        return ret

    def get_fft(self):
        data = self.get_float() * self.hamming
        return fftpack.fft(data)[:self.CHUNK//2]


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    ai = AudioInput()
    ret = ai.get_fft()
    plt.plot(ret)
    plt.show()
