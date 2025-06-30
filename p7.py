p7    
import numpy as np
import matplotlib.pyplot as plt

# Generate time series data
np.random.seed(0)
time_series = np.cumsum(np.random.randn(100)) + 50

# Moving average function
def moving_average(data, window_size):
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

# Compute moving average
window_size = 5
ma = moving_average(time_series, window_size)

# Plot time series and moving average
plt.figure(figsize=(10, 5))
plt.plot(time_series, label='Original Time Series')
plt.plot(range(window_size-1, len(ma)+window_size-1), ma, label='Moving Average', color='red')
plt.xlabel("Time")
plt.ylabel("Value")
plt.title("Simple Moving Average")
plt.legend()
plt.show()

