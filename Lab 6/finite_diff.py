import numpy as np


def forward_diff(f, s, h):
    return (f(s + h) - f(s)) / h

def centered_diff(f, s, h):
    return (f(s + h) - f(s - h)) / (2 * h)

f = lambda x: np.cos(x)
s = 3 * np.pi / 4
s_prime = -np.sqrt(2) / 2
h = 0.01 / 2 ** np.arange(0, 10)


fprime_1 = forward_diff(f, s, h)
fprime_2 = centered_diff(f, s, h)


print("forward difference: ", fprime_1)
print("digits of accuracy " ,-np.log10(np.abs(s_prime - fprime_1)))
print("centered difference: ", fprime_2)
print("digits of accuracy " ,-np.log10(np.abs(s_prime - fprime_2)))
print(np)

'''
Using our log differences, we see that around pi/2 they both see to be linear. However if we experiment with other points, we see that
centered difference behaves more superlinearly that linear, as it gains more digits of accuracy than forward difference.
'''