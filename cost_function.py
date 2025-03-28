import numpy as np

# Actual and predicted values
y_actual = np.array([3, -0.5, 2, 7])
y_predicted = np.array([2.5, 0.0, 2, 8])

# Compute Mean Squared Error
mse = np.mean((y_actual - y_predicted) ** 2)
print("Mean Squared Error:", mse)
