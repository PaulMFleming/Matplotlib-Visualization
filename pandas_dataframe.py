import pandas 
import matplotlib.pyplot as plt
from matplotlib import style

style.use('dark_background')

web_stats = {'Day':[1,2,3,4,5,6],
            'Visitors':[43,34,65,56,29,76],
            'Bounce Rate':[65,67,78,65,45,52]}

df = pandas.DataFrame(web_stats)
df.set_index('Day', inplace=True) # set the Day column as the index
                                  # otherwise pandas will create an index

df.plot()
plt.show()