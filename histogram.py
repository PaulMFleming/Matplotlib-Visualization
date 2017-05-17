import matplotlib.pyplot as plt

population_ages = [22,55,62,76,42,110,97,111,115,3,2,9,83,44,57,96,34,27,23]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()