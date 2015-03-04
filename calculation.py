import numpy as np


def root_mean_square(array):
    return (np.mean(array ** 2)) ** 0.5


def normalized(array):
    return array / max(array)


def spectrum(array):
    print("*  fft")
    array *= np.hamming(len(array))  # window
    complex_array = np.fft.fft(array)  # fft
    complex_array = complex_array[:len(complex_array) // 2]  # - mirror part
    array = list(map(abs, complex_array))  # complex to double
    print('** ' + str(len(array)))
    return array


def cepstrum(array):
    print("*  fft(fft)")
    array *= np.hamming(len(array))
    complex_array = np.fft.fft(array)
    array = abs(complex_array)
    array = array[:(len(array) // 2)]
    # array = np.log10(array)
    complex_array = np.fft.ifft(array)
    array = abs(complex_array)
    array = array[:(len(array) // 2)]
    return array


def energy(array, size_chunk):
    list_energy = list()
    for i in range(len(array) // size_chunk):
        l = array[i * size_chunk:i * size_chunk + size_chunk]
        list_energy.append(root_mean_square(l))
    l = list()
    for i in range(len(list_energy) - 1):
        l.append(sum(list_energy[i:i + 2]) / 2)
    return l


def derivative(array):
    d = list()
    for i in range(len(array) - 1):
        d.append(array[i + 1] - array[i])
    return d


def max_value(array, size_chunk):
    array = abs(array)
    maximum = list()
    for i in range(len(array) // size_chunk):
        maximum.append(max(array[i * size_chunk:i * size_chunk + size_chunk]))

    der = derivative(maximum)
    second_der = derivative(der)

    array = list(map(abs, second_der))
    average = max(array) / 2

    print("Ave: ", average)

    count = 0
    for x in array:
        count += x - average if x > average else 0

    print('Count: ', count)

    average = 0
    count_average = 0
    for i in range(len(array) - 2):
        if array[i] < array[i + 1] > array[i + 2]:
            average += array[i + 1]
            count_average += 1
    average /= count_average
    print('Ave: ', average)

    count = 0
    for x in array:
        count += x - average if x > average else 0
    print('Count: ', count)

    return array