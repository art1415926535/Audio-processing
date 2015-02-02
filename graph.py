import datetime
from logging import critical

from PIL import Image, ImageDraw


def create_2d_graph(array, path='/img/', name=None,
                    fill=(0, 0, 255, 255), outline=(0, 0, 0, 255)):
    try:
        width = len(array)
        height = 100  # len(array[0])
    except TypeError:
        critical('NEED ARRAY')
        return None

    # create image
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    max_y = max(array)
    points = [(x, y / max_y * height) for y, x in zip(array, range(len(array)))]
    points.append((width, height))
    points.append((0, height))

    draw.polygon(points, fill=fill, outline=outline)

    del draw

    if name is None:
        name = datetime.datetime.now().time().isoformat()[:-7]  # -msec
    full_path = path + name + '.png'

    image.save(full_path, "PNG")

    return full_path


def create_3d_graph(array, path='/img/', name=None):
    try:
        width = len(array)
        height = len(array[0])
    except TypeError:
        critical('NEED 2D ARRAY')
        return None

    # create image
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    a = []
    for i in array:
        for j in i:
            a.append(j)

    max_z = max(a)

    for row in range(len(array)):
        for cell in range(len(array[0])):
            draw.point((row, cell),
                       (int(array[row][cell] / max_z * 255), 0, 0, 255))  # FIXME:  array[row][cell] to NORMAL

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

    y_points = 40000
    y = [random.randint(0, 100) / 100 * x for x in range(y_points)]

    z_points = 4000
    z = []
    n = random.randint(3, 200)
    for i in range(n):
        z += [[random.randint(0, 100) / 100 * x for x in range(100)]] * (z_points // n)


    t_graph = time.time()
    create_2d_graph(y, '', 'foo')
    print('time creating 2d graph:{} with {} points'.format(time.time() - t_graph, y_points))

    t_graph = time.time()
    create_3d_graph(z, '', 'foo')
    print('time creating 3d graph:{} with {} points'.format(time.time() - t_graph, z_points * 100))