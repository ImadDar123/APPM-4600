import numpy as np
import matplotlib.pyplot as plt
import math

#sum of t(k)y(k) for (a)
t = np.arange(0,np.pi, np.pi/30)
y = np.cos(t)
S = np.sum(t * y)
print(f"the sum is {S}")


# constants for (b)
R = 1.2
delta_r = 0.1
f = 15
p = 0

# figure with two parametric curves for (b)
theta = np.linspace(0, 2* np.pi, 1000)
x = R * (1 + delta_r * np.sin(f * theta + p)) * np.cos(theta)
y = R * (1 + delta_r * np.sin(f * theta + p)) * np.sin(theta)

# plt.plot(x, y)
# plt.show()

# second figure for (b)
delta_r = 0.05
p = np.random.uniform(0, 2)

for i  in range(1, 10):
    R = i
    f = 2 + i
    x = R * (1 + delta_r * np.sin(f * theta + p)) * np.cos(theta)
    y = R * (1 + delta_r * np.sin(f * theta + p)) * np.sin(theta)
    plt.plot(x, y)
    
plt.show()

