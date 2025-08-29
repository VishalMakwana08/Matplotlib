import pylab as plt


#plot 1:
x = [0, 1, 2, 3]
y = [3, 8, 1, 10]
plt.suptitle('Multiple Subplots Example', fontsize=16)
plt.subplot(3, 3, 1)
plt.plot(x,y)
plt.title('First Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
#plot 2:
x = [0, 1, 2, 3]
y = [10, 20, 30, 40]

plt.subplot(3, 3, 2)
plt.plot(x,y)
plt.title('Second Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
#plot 3:
x = [0, 1, 2, 3]
y = [30, 10, 40, 20]
plt.subplot(3, 3, 3)
plt.plot(x,y)       
plt.title('Third Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
#plot 4:
x = [0, 1, 2, 3]
y = [10, 30, 20, 40]
plt.subplot(3, 3, 4)
plt.plot(x,y)
plt.title('Fourth Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
#plot 5:
x = [0, 1, 2, 3]
y = [40, 30, 20, 10]
plt.subplot(3, 3, 5)
plt.plot(x,y)
plt.title('Fifth Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
#plot 6 
x = [0, 1, 2, 3]
y = [20, 10, 40, 30]
plt.subplot(3, 3, 6)        
plt.plot(x,y)
plt.title('Sixth Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()

plt.show()