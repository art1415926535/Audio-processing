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

        self.nchannels, self.sampwidth, self.framerate, \
        self.nframes, self.comptype, self.compname = self.__wav.getparams()

        self.content = self.__wav.readframes(self.nframes)
        self.samples = np.fromstring(self.content, dtype=types[self.sampwidth])

        self.__channels = []

        for n in range(self.nchannels):
            self.__channels.append(self.samples[n::self.nchannels])

    def get_channel(self, channel=0):
        return self.__channels[channel]

    def normalization_channel(self, channel=0):
        print('start')
        array = self.get_channel(channel)
        maximum = max(array)
        print(len(array), maximum)
        a = array / maximum
        print('end')
        return a


if __name__ == '__main__':
    w = Wave(r'C:\Users\dark\Documents\Project\test_idea_about_beat\beat\music\The Game.wav')

    print(w.get_channel())
    print(w.normalization_channel())
