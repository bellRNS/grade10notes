import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import matplotlib.pyplot as plt

""" make sure you are running the file from the same 
directory as your csv file"""

data = pd.read_csv('shootings.csv')     #loading it in 

data.head(10)                           # first 10 lines of data 
data.columns                            #prints out all column headers

""" before doing anything at all, I want to know some more about
    the data that we are using. EX. what type is each?"""

data.dtypes                             #prints out data types of columns


#manner of death pie chart
df1 = data['manner_of_death'].value_counts().reset_index()  #note that 'data' at the beginning is not a keyword, it is my imported data set. 
df1.columns = ['manner_of_death','count']
fig = px.pie(                       #makes a pie graph
    df1,                            #using the appropriate data 
    values = 'count',               #values to be plotted
    names = 'manner_of_death',      #essentially the independent variable 
    title = 'Manner of Death',      #title for graph
    width = 500,                    #massaging graph size 
    height = 500
)
fig.show()                          #displays the plot 

#weapon threat 
df2 = data['armed'].value_counts().reset_index()
df2.columns = ['armed', 'count']
df2 = df2.sort_values('count')
fig = px.bar(                #makes a bar graph 
    df2.tail(25),            #takes the top 25 instances 
    x = 'count',             #variable to choose
    y = 'armed',             #variable to choose
    orientation = 'h',       #sets horizont or vert
    title='Weapon Threat',   #sets title 
    width = 800,
    height = 800,
)
fig.show()


#one of the best things about ipython is that you can run this file, 
#and it will spit out your graphics on a web browser all at once on different tabs! 


"""

Your tasks: 

-Plot everything from the kaggle link given.
https://www.kaggle.com/isaienkov/us-police-shootings-visualization-and-analysis

-Understand some of the ways we manipulate data to get what we want
    -Example notice how the first two plots used value_counts()
        and set the column names. We create small data frames for graphing. 

-Your assignment from Bell will be to analyze a given data set much like this! 

-Expect a data set no harder or no simpler than the one you are using. 

-Email Bell three areas of data interest in your life. I will try my best 
    to give you a data set that means something to you for your assignment.

"""

