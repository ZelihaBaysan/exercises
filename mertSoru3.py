import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2.5, 10)
y = (0.5 * x**2) * np.cos(x**2)

plt.scatter(x, y, s=1)
plt.grid(True)
plt.show()

roots = []

for i in range(len(y) - 1):
    if (y[i] * y[i+1] < 0 or y[i]==0):
       
        roots.append(y[i])

print("Kökler:", roots)  
