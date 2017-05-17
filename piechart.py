import matplotlib.pyplot as plt 

slices = [7,2,2,13] # specify the size of the slices
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0,0.1,0,0),
        autopct='%1.f%%') # overlays the percentages on the graph

plt.title('Interesting Graph\nCheck it out')
plt.show()