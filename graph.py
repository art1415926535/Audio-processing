import datetime

import matplotlib.pyplot as plt


def new_graph(array, path='/img/', name=None):
    if name is None:
        name = datetime.datetime.now().time().isoformat()[:-7]  # -msec

    plt.axes().get_xaxis().set_visible(False)  # del labels
    plt.axes().get_yaxis().set_visible(False)  # del labels
    plt.tight_layout()  # del gray area around plot

    plt.imshow(array, interpolation='none')

    p = path + name + '.png'
    plt.savefig(p, bbox_inches='tight', pad_inches=0)

    return p


if __name__ == '__main__':
    import random
    import time

    t_rand = time.time()
    z = [[random.randint(0, 30) for _ in range(1000)],
         [random.randint(0, 30) for _ in range(1000)]] * 2000
    print("t rand:", time.time() - t_rand)
    print(len(z), len(z[0]))

    t_graph = time.time()
    new_graph(z, '', 'foo')
    print('time creating graph:', time.time() - t_graph)