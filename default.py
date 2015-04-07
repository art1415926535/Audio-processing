from wave_pars import Wave
import calculation
import numpy as np

path = 'Отдельно звук Р/Новые/.wav'
wave = Wave(path)
c = wave.channel[::]

array_np = np.array(c, dtype=np.float64)

#array_np /= max([abs(i) for i in array_np])

plot.set_data(array_np) 
plot.set_title(path)