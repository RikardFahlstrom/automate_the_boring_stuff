import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_values,squares,linewidth=5)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)

plt.show()

# Below prints a specific value in a scatter plot

plt.scatter(2,4, s=200)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()

# Below prints a scatter plot where xy-coordinates sets automatically
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, edgecolor='none', s=40, c=y_values, cmap=plt.cm.Blues)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set the range for each axis.
plt.axis([0,1100, 0, 1100000])

plt.savefig('squares_plot.png', bbox_inches='tight')
