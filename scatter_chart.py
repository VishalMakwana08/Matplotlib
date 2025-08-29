import pylab as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.scatter(x, y, marker='o', linestyle='-', label='Numbers', s=100, edgecolor='k', alpha=0.7, cmap='viridis', c=y)
plt.title('Scatter Chart Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid()
plt.show()  # Display the plot
plt.savefig('scatter_chart.png')  # Save the plot as a PNG file
# This code creates a simple line chart using Matplotlib and saves it as a PNG file.