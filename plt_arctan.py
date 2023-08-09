import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 101)
plt.plot(x, np.arctan(x))
plt.xlabel('x')
plt.ylabel('arctan(x)')
plt.axis('tight')
plt.show()
