
#Installing the pytrends library to interact with Google Trends API
!pip install pytrends

# Importing the pandas library for data manipulation and analysis
import pandas as pd

# Importing the TrendReq class from the pytrends library to request Google Trends data
from pytrends.request import TrendReq

# Importing the pyplot module from matplotlib for creating visualizations
import matplotlib.pyplot as plt

# Importing time module to handle time-related tasks
import time

# Creating a TrendReq object with US English settings and a timezone offset of 300 minutes (i.e., Eastern Time)
Trending_topics = TrendReq(hl='en-US', tz=300)

# Building payload for Google Trends data on "Concert" over the past 12 months and adding a delay of 5 seconds to avoid rate limiting
kw_list=["Concert"]
Trending_topics.build_payload(kw_list,cat=0, timeframe='today 12-m')
time.sleep(5) 

# Fetching Google Trends data for "Concert", sorting by popularity, selecting top 20 records, and printing the result
data = Trending_topics.interest_over_time()
data = data.sort_values(by="Concert", ascending = False)
data = data.head(20)
time.sleep(5)
print(data)

# Fetching regional interest data for "Concert", sorting by popularity, selecting top 10 regions, and printing the result
data = Trending_topics.interest_by_region()
data = data.sort_values(by="Concert", ascending = False)
data = data.head(10)
time.sleep(5)
print(data)

# Resetting the index, plotting regional interest data for "Concert" as a bar chart, and displaying the plot with a specific style
data.reset_index().plot(x='geoName', y='Concert', figsize=(8,3), kind="bar")
plt.style.use('fivethirtyeight')
plt.show()

# Fetching the top trending charts for 2023 globally, and displaying the top 10 entries
df = Trending_topics.top_charts(2023, hl='en-US', tz=300, geo='GLOBAL')
df.head(10)

# Attempting to fetch related queries for "Concert" and handling potential errors
try:
    Trending_topics.build_payload(kw_list=['Concert'])
    related_queries = Trending_topics.related_queries()
    related_queries.values()
except (KeyError, IndexError):
    print("Nothing found")

# Fetching keyword suggestions for "Concert" and converting the results to a DataFrame, then dropping the 'mid' column
keywords = Trending_topics.suggestions(
  keyword='Concert')
df = pd.DataFrame(keywords)
df.drop(columns= 'mid') 


