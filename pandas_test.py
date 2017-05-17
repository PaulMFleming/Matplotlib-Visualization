import datetime 
import pandas
import matplotlib.pyplot as plt
from pandas_datareader import data # pulls data from the web
from matplotlib import style

style.use('fivethirtyeight') # helps us quickly make our graph look good

# create start and end variables
# we'll pull data from between these dates
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 8, 22)

# create a dataframe:
# pull info from the Google Finance API
# store the data in the df variable 
# calling this variable 'df' is the standard
df = data.DataReader("F", "google", start, end)

print df.head() # print out the first 5 rows of the dataframe

df['High'].plot()
plt.legend()
plt.show()