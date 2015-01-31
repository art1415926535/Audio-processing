import matplotlib.pyplot as plt

z = [[1, 2, 3, 4],
     [2, 3, 4, 5]]

plt.axes().get_xaxis().set_visible(False)  # del labels
plt.axes().get_yaxis().set_visible(False)  # del labels
plt.tight_layout()  # del gray area around plot

plt.imshow(z)
plt.savefig('foo.png', bbox_inches='tight', pad_inches=0)
