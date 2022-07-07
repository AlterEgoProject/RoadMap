import numpy as np
from numpy.fft import ifft
import pyaudio
import struct

fs = 44100
chunk = 1024
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=fs,
                output=True)


def voice():
    sec = 5
    hlen = 200
    hamming = np.hamming(hlen)
    for i in range(int(sec*fs/chunk)):
        chunk_data = np.random.random(chunk) / 5
        for j in range(int(chunk/hlen)):
            data = hamming * chunk_data[j*hlen:(j+1)*hlen]
            s = [int(x * 32767.0) for x in data]
            bin = struct.pack('h' * len(s), *s)
            stream.write(bin)

        # data = np.random.random(chunk) / 5
        # F = np.ones(chunk)
        # data = ifft(F)
        # s = [int(x * 32767.0) for x in data]
        # bin = struct.pack('h' * len(s), *s)
        # stream.write(bin)


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    voice()
