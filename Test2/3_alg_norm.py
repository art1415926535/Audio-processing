# 2015-04-03 18:27:14
from wave_pars import Wave
import calculation
import numpy as np


wave = Wave('Отдельно звук Р/Новые/3.wav')
c = wave.channel[::]

array_np = np.array(c, dtype=np.float64)

#array_np /= max([abs(i) for i in array_np])

plot.set_data(array_np)