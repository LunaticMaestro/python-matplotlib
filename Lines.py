# Rudimentary Files
import numpy as np
import matplotlib.pyplot as plt

# Line Plots
xvals = np.linspace(start=-2, stop=4, num=50)
yvals = np.cos(xvals)
plt.plot(xvals, yvals, label="Cosine Values")
plt.legend()
plt.grid()
plt.show()