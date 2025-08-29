import pylab as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.hist(y, bins=5, color='blue', edgecolor='black', alpha=0.5)
plt.title('Histogram Chart Example')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()  # Display the plot
plt.savefig('histogram_chart.png')  # Save the plot as a PNG file           