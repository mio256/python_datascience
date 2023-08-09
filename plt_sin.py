import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 101)
plt.plot(x, np.sin(x))
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
plt.axis('tight')
plt.show()
