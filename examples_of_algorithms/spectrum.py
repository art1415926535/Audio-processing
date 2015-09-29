# 2015-03-06 13:05:28
from wave_parser import Wave
import calculation

wave = Wave('{wav}')
c = wave.channel

width = len(c) // 1000
array = []

for i in range(width):
    a = calculation.spectrum(
        c[i / width * len(c):(i + 1) / width * len(c)]
    )
    array.append([int(i) for i in a])

plot.set_data(array)