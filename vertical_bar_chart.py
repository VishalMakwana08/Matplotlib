import pylab as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.bar(x, y, color='blue', edgecolor='black', alpha=0.7,width=0.5)
plt.title('Bar Chart Example')  
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()  # Display the plot
plt.savefig('bar_chart.png')  # Save the plot as a PNG file