import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 301)
plt.plot(x, np.arcsin(x))
plt.xlabel('x')
plt.ylabel('arcsin(x)')
plt.axis('tight')
plt.show()
