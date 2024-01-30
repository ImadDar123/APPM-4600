import numpy as np
import matplotlib.pyplot as plt



# # problem 1


# x = np.arange(1.920, 2.080, 0.001)

# f = x ** 9 - 18 * x ** 8 + 144 * x ** 7 - 672 * x ** 6 + 2016 * x ** 5 - 4032 * x ** 4 + 5376 * x ** 3 - 4608 * x ** 2 + 2304 * x -512

# g = (x - 2) ** 9

# plt.plot(x, f)
# plt.plot(x, g)

# plt.show()









# # problem 3b

# # Function to calculate the difference between expressions
def expression_difference(x, delta):
    original_expression = np.cos(x + delta) - np.cos(x)
    simplified_expression = -2 * np.sin(x + delta/2) * np.sin(delta/2)
    return original_expression - simplified_expression

# Values of x
x_values = [np.pi, 10 ** 6]

# Values of delta
deltas = np.logspace(-16, 2, num=100)

# # Plotting
# plt.figure(figsize=(10, 6))

# for x in x_values:
#     differences = [expression_difference(x, delta) for delta in deltas]
#     plt.semilogx(deltas, differences, label=f'x = {x}')

# plt.title('Difference between Expressions')
# plt.xlabel('Delta (log scale)')
# plt.ylabel('Difference')
# plt.legend()
# plt.grid(True)
# plt.show()







# problem 3c

# Function to calculate the Taylor expansion approximation
def taylor_approximation(x, delta):
    first_derivative = -np.sin(x)
    second_derivative = -np.cos(np.random.uniform(x, x + delta))  # Choose a random xi between x and x + delta
    return delta * first_derivative + (delta**2) / 2 * second_derivative

# Values of x and delta
x_values = [np.pi, 10 ** 6]
delta_values = np.logspace(-16, 2, num=100)

# Plotting
plt.figure(figsize=(10, 6))

for x in x_values:
    taylor_approximations = [taylor_approximation(x, delta) for delta in delta_values]
    plt.semilogx(delta_values, taylor_approximations, label=f'Taylor Approximation, x = {x}')

# Adding the expressions from part (b)
for x in x_values:
    differences_part_b = [expression_difference(x, delta) for delta in delta_values]
    plt.semilogx(delta_values, differences_part_b, label=f'Part (b) Difference, x = {x}', linestyle='dashed')

plt.title('Comparison of Taylor Expansion Approximation and Part (b)')
plt.xlabel('Delta (log scale)')
plt.ylabel('Approximation/Difference')
plt.legend()
plt.grid(True)
plt.show()
