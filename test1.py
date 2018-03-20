import matplotlib.pyplot as plt
import numpy as np

A = np.random.rand(5, 5)
plt.figure(1)
plt.imshow(A, interpolation='nearest')
plt.grid(True)

plt.show()