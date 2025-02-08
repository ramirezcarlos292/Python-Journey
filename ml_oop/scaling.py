import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# Generate sample data with outliers
np.random.seed(0)
data = np.random.randn(100, 2)  # Normally distributed data
data_with_outliers = np.copy(data)
data_with_outliers[::10] = np.array([10, 10])  # Add outliers

# Apply scalers
standard_scaler = StandardScaler()
data_standard_scaled = standard_scaler.fit_transform(data_with_outliers)

min_max_scaler = MinMaxScaler()
data_min_max_scaled = min_max_scaler.fit_transform(data_with_outliers)

robust_scaler = RobustScaler()
data_robust_scaled = robust_scaler.fit_transform(data_with_outliers)

# Plot the original and scaled data
fig, axes = plt.subplots(2, 2, figsize=(12, 12))
axes = axes.flatten()

axes[0].scatter(data_with_outliers[:, 0], data_with_outliers[:, 1], color='blue', label='Original')
axes[0].set_title('Original Data with Outliers')

axes[1].scatter(data_standard_scaled[:, 0], data_standard_scaled[:, 1], color='green', label='Standard Scaled')
axes[1].set_title('Standard Scaled Data')

axes[2].scatter(data_min_max_scaled[:, 0], data_min_max_scaled[:, 1], color='red', label='Min-Max Scaled')
axes[2].set_title('Min-Max Scaled Data')

axes[3].scatter(data_robust_scaled[:, 0], data_robust_scaled[:, 1], color='purple', label='Robust Scaled')
axes[3].set_title('Robust Scaled Data')

for ax in axes:
    ax.legend()

plt.tight_layout()
plt.show()
