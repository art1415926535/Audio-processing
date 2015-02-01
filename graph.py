import datetime
from logging import critical

import matplotlib.pyplot as plt
from PIL import Image, ImageDraw


def create_2d_graph(array, path='/img/', name=None):
    if name is None:
        name = datetime.datetime.now().time().isoformat()[:-7]  # -msec

    plt.axes().get_xaxis().set_visible(False)  # del labels
    plt.axes().get_yaxis().set_visible(False)  # del labels
    plt.tight_layout()  # del gray area around plot

    plt.plot(array)  # , interpolation='none')

    p = path + name + '.png'
    plt.savefig(p, dpi=100, bbox_inches='tight', pad_inches=0)

    return p


def create_3d_graph(array, path='/img/', name=None):
    try:
        width = len(array)
        height = len(array[0])
    except TypeError:
        critical('NEED 2D ARRAY')
        return 1

    # create image
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    del draw

    # save image
    if name is None:
        name = datetime.datetime.now().time().isoformat()[:-7]  # -msec
    full_path = path + name + '.png'
    image.save(full_path, "PNG")

    return full_path

if __name__ == '__main__':
    import random
    import time

    '''
    t_rand = time.time()
    width = 300
    height = 900
    z = [[random.randint(0, 30) for _ in range(width)]] * (height // 3) + \
        [[random.randint(0, 30) for _ in range(width)]] * (height // 3) + \
        [[random.randint(0, 30) for _ in range(width)]] * (height // 3)
    print("t rand:", time.time() - t_rand)
    print(len(z), len(z[0]))
    '''
    z = [random.randint(0, 100) / 100 * x for x in range(2000)]
    t_graph = time.time()
    create_2d_graph(z, '', 'foo')
    print('time creating graph:', time.time() - t_graph)