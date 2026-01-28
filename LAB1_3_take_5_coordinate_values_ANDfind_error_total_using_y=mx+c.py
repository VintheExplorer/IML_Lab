import numpy as np
import matplotlib.pyplot as plt

x_values = np.array([1, 2, 3, 4, 5])
actual_y = np.array([4, 5, 8, 9, 11])

slope = 2
intercept = 1

predicted_y = slope * x_values + intercept

errors = actual_y - predicted_y

total_absolute_error = np.sum(np.abs(errors))
total_squared_error = np.sum(errors ** 2)
mean_squared_error = np.mean(errors ** 2)

print("Predicted values:", predicted_y)
print("Errors:", errors)
print("Total Absolute Error:", total_absolute_error)
print("Total Squared Error:", total_squared_error)
print("Mean Squared Error:", mean_squared_error)

plt.figure()
plt.scatter(x_values, actual_y)
plt.plot(x_values, predicted_y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Regression Model y = mx + c")
plt.show()
