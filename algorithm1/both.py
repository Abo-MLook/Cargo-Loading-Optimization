import matplotlib.pyplot as plt
import numpy as np

# Common input sizes
input_sizes = np.array([3, 15, 21, 25, 30])

# --- Native Recursive Algorithm Data ---
recursive_times = np.array([0.000006, 0.0059149265, 0.3666234016, 6.125460, 192])
log_recursive = np.log(recursive_times)
coeffs_recursive = np.polyfit(input_sizes, log_recursive, deg=2)

def recursive_model(x):
    return np.exp(coeffs_recursive[0]*x**2 + coeffs_recursive[1]*x + coeffs_recursive[2])

# --- Bottom-Up DP Algorithm Data ---
dp_times = np.array([0.0000343323, 0.0001351833, 0.0020546913, 0.0029530525, 0.0031647018])
coeffs_dp = np.polyfit(input_sizes, dp_times, deg=1)

def dp_model(x):
    return coeffs_dp[0]*x + coeffs_dp[1]

# --- Plot Both ---
x_smooth = np.linspace(min(input_sizes), max(input_sizes), 500)

plt.figure(figsize=(12, 7))

# Recursive plot
plt.plot(x_smooth, recursive_model(x_smooth), label='Native Recursive ', color='red')
plt.scatter(input_sizes, recursive_times, color='red', marker='o', zorder=5)

# DP plot
plt.plot(x_smooth, dp_model(x_smooth), label='Bottom-Up DP ', color='blue')
plt.scatter(input_sizes, dp_times, color='blue', marker='s', zorder=5)

# Add labels to points
for x, y in zip(input_sizes, recursive_times):
    label = f'{y:.2f}s' if y >= 1 else f'{y:.5f}s'
    plt.text(x, y, label, fontsize=9, ha='left', va='bottom', color='red')

for x, y in zip(input_sizes, dp_times):
    label = f'{y:.2f}s' if y >= 1 else f'{y:.9f}s'
    plt.text(x, y, label, fontsize=9, ha='right', va='top', color='blue')

# Labels, legend, and grid
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Comparison of Knapsack Algorithms: Recursive vs Bottom-Up DP')
plt.grid(True)
plt.xticks(input_sizes)
plt.ylim(0, 200)
plt.legend()

plt.show()
