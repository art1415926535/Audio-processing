# 2015-03-06 14:58:47
from wave_parser import Wave
import calculation

wave = Wave('{wav}')
c = wave.channel[::10]

array = calculation.energy(c, 1000)
plot.set_data(array)