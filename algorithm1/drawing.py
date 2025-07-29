import matplotlib.pyplot as plt
import numpy as np

# Original data points
input_sizes = np.array([3, 15, 21, 25, 30])
execution_times = np.array([0.000006, 0.0059149265, 0.3666234016, 6.125460, 192])

# Take log of execution times for exponential fitting
log_times = np.log(execution_times)

# Fit a polynomial to the log of the data (this gives exponential growth)
coeffs = np.polyfit(input_sizes, log_times, deg=2)  # quadratic in exponent

# Define the exponential model
def exp_model(x):
    return np.exp(coeffs[0]*x**2 + coeffs[1]*x + coeffs[2])

# Smooth x range
x_smooth = np.linspace(min(input_sizes), max(input_sizes), 500)
y_smooth = exp_model(x_smooth)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(x_smooth, y_smooth, label='Exponential Fit Curve', color='blue')
plt.scatter(input_sizes, execution_times, color='red', zorder=5)

# Add labels to original points
for x, y in zip(input_sizes, execution_times):
    label = f'{y:.2f}s' if y >= 1 else f'{y:.6f}s'
    plt.text(x, y, label, fontsize=9, ha='left', va='bottom')

# Labels and style
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time Growth of Native Recursive Knapsack (Exponential Curve Fit)')
plt.grid(True)
plt.xticks(input_sizes)
plt.legend()

# Show plot
plt.show()
