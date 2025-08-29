import pylab as plt

qty = [2, 3, 5]
labels_list = ['Apple', 'Banana', 'Orange']
plt.pie(qty, labels=labels_list, startangle=180,explode=(0,0,0.1))
plt.title('Pie Chart Example')
plt.legend(title="Fruits", loc="best")
plt.show()  # Display the plot
plt.savefig('pie_chart.png')  # Save the plot as a PNG file