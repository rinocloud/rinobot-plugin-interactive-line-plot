import numpy as np

x = np.linspace(0, 100, 500)
y1 = np.sin(x/10) + np.random.random_sample(size=500)/10
y2 = np.sin(x/10 + 10) + np.random.random_sample(size=500)/10

np.savetxt('examples/data.txt', np.vstack((x, y1, y2)).T)
