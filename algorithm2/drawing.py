import matplotlib.pyplot as plt
import numpy as np

# New data (likely linear or close to linear)
input_sizes = np.array([3, 15, 21, 25, 30])
execution_times = np.array([
    0.0000343323,
    0.0001351833,
    0.0020546913,
    0.0029530525,
    0.0031647018
])

# Fit a linear model
coeffs = np.polyfit(input_sizes, execution_times, deg=1)

# Define linear model
def linear_model(x):
    return coeffs[0]*x + coeffs[1]

# Smooth x range
x_smooth = np.linspace(min(input_sizes), max(input_sizes), 500)
y_smooth = linear_model(x_smooth)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(x_smooth, y_smooth, label='n * m', color='green')
plt.scatter(input_sizes, execution_times, color='red', zorder=5)

# Add labels to original points
for x, y in zip(input_sizes, execution_times):
    label = f'{y:.2f}s' if y >= 1 else f'{y:.9f}s'
    plt.text(x, y, label, fontsize=9, ha='left', va='bottom')

# Labels and style
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time Growth of Bottom-Up DP Knapsack Algorithm')
plt.grid(True)
plt.xticks(input_sizes)
plt.ylim(0, 200)  # Force Y-axis to match the previous plot
plt.legend(loc='upper left')

# Show plot
plt.show()
