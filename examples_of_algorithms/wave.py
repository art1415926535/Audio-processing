# 2015-03-06 12:52:02
from wave_parser import Wave
import calculation

wave = Wave('{wav}')
c = wave.channel
plot.set_data(c[::500])