import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def main(filepath):
    filename_without_ext = os.path.splitext(filepath)[0]
    data = np.loadtxt(filepath)

    x = data[:, 0]
    y = data[:, 1:]
    plt.plot(x, y)
    plt.savefig(filename_without_ext + '.png')


if __name__ == "__main__":
    main(sys.argv[1])
