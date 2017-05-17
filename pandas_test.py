import datetime 
import pandas

from pandas_datareader import data # pulls data from the web

# create start and end variables
# we'll pull data from between these dates
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 8, 22)

# create a dataframe:
# pull info for Exxon from the Yahoo Finance API
# store the data in the df variable 
# calling this variable 'df' is the standard
df = data.DataReader("F", "google", start, end)

print df.head() # print out the first 5 rows of the dataframe