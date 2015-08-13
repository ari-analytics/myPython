import numpy as np
import matplotlib.pyplot as plt
import mpld3

x = np.linspace(0,10,100)
y = np.sin(x)
plt.plot(x,y)
mpld3.show()

