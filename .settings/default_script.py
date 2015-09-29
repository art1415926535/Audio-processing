from wave_parser import Wave
import calculation
import numpy as np


wave = Wave('{wav}')
c = wave.get_channel(0)

array_np = np.array(c, dtype=np.float64)
array_np /= max([abs(i) for i in array_np])

plot.set_data(array_np)