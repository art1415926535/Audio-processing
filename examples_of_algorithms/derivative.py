# 2015-03-06 12:52:43
from wave_parser import Wave
import calculation

wave = Wave('{wav}')
c = wave.channel[::10000]

array = calculation.derivative(c)
array = [abs(a) for a in array]

plot.set_data(array)