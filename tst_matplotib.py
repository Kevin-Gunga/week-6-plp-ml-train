# Matplotlib is a popular open-source data visualization library for Python. It provides a wide range of tools for creating static, animated, and interactive visualizations in Python.
# Some of the key features of Matplotlib include:

# Line plots: used to plot continuous data as a series of connected points.
# Scatter plots: used to plot data points as individual dots or markers.
# Bar charts: used to plot categorical data as bars.
# Histograms: used to plot the distribution of a set of continuous data.
# Heatmaps: used to plot data as a color-coded grid.
# Contour plots: used to plot data as a series of contours or lines.

# line plot
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('line plot of sin(x)')
plt.show()

# scatter plot
x = np.random.randn(100)
y = np.random.randn(100)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('scatter plot of random data')
plt.show()

# bar chart
x = ['Apples', 'Bananas', 'Oranges']
y = [10, 7, 15]

plt.bar(x, y)
plt.xlabel('Fruit')
plt.ylabel('Quantity')
plt.title('Bar chart of fruit quantities')
plt.show()

# histogram
data = np.random.randn(1000)

plt.hist(data, bins=30)
plt.xlabel('value')
plt.ylabel('frequency')
plt.title('histogram of random data')
plt.show()

# subplots
x = np.linspace(0,10,100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, (ax1, ax2) = plt.subplots(2,1, figsize=(8,6))

ax1.plot(x, y1)
ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)')
ax1.set_title('line plot of sin(x)')

ax2.plot(x, y2)
ax2.set_xlabel('x')
ax2.set_ylabel('cos(x)')
ax2.set_title('line plot of cos(x)')

plt.tight_layout()
plt.show()
