import logging

import wave
import numpy as np


types = {
    1: np.int8,
    2: np.int16,
    4: np.int32
}


class Wave():
    def __init__(self, path):
        self.__wav = wave.open(path, mode='r')

        self.count_channels = self.__wav.getnchannels()
        self.width_of_sample = self.__wav.getsampwidth()
        self.rate_of_frame = self.__wav.getframerate()
        self.count_of_frames = self.__wav.getnframes()
        self.compression_type = self.__wav.getcomptype()
        self.compression_name = self.__wav.getcompname()
        logging.info("{}:\n"
                     "count channels: {}\n"
                     "width of sample: {}".format(path, self.count_channels, self.width_of_sample))

        self.content = self.__wav.readframes(self.count_of_frames)
        self.samples = np.fromstring(self.content, dtype=types[self.width_of_sample])

        self.__channels = [self.samples[n::self.count_channels] for n in range(self.count_channels)]
        self.channel = self.__channels[0]

    def get_channel(self, channel):
        return self.__channels[channel]

    def normalized_channel(self, channel):
        array = self.__channels[channel]
        maximum = max(array)
        return array / maximum


if __name__ == '__main__':
    import sys

    w = Wave(sys.argv[1])

    c = w.channel
    print(c[len(c) / 2 - 5:len(c) / 2 + 5])
    print(w.normalized_channel(0)[len(c) / 2 - 5:len(c) / 2 + 5])
