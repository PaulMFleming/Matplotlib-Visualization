import matplotlib.pyplot as plt

# coordinates for first line
x = [1,2,3]
y = [5,7,4]

# coordinates for the second line
x2 = [1,2,3]
y2 = [10,14,12]

# plot both lines AND add the parameter 'label'
plt.plot(x, y, label='First Line')
plt.plot(x2, y2, label='Second Line')

plt.xlabel('Plot Number') # assign label to x axis
plt.ylabel('Important var') # assign label to y axis
plt.title('Interesting Graph\nCheck it out') # assign the plots title
plt.legend() # invokes a legend
plt.show() # show graph on screen

