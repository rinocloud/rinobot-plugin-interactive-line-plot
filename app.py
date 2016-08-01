import sys
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

output_format = '.png'

matplotlib.rcParams['savefig.dpi'] = 2 * matplotlib.rcParams['savefig.dpi']

def main(filepath):
    filename_without_ext = os.path.splitext(filepath)[0]
    data = np.loadtxt(filepath)
    x = data[:, 0]
    y = data[:, 1:]
    plt.plot(x, y)
    plt.savefig(filename_without_ext + output_format)

if __name__ == "__main__":
    main(sys.argv[1])
