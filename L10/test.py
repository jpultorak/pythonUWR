import numpy as np
import matplotlib.pyplot as plt 

a = np.diag([100 for _ in range(100)])

plt.matshow(a, vmin = 0, vmax=255)

plt.show()
