import pylab as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o', linestyle='-', color='b', label='Numbers')
plt.title('Line Chart Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()  # Display the plot
plt.savefig('line_chart.png')  # Save the plot as a PNG file
# This code creates a simple line chart using Matplotlib and saves it as a PNG file.