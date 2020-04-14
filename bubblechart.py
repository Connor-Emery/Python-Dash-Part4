import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/Weather2014-15.csv')
# Removing empty spaces
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating sum of number of cases group by Month Column
new_df = df.groupby(['month']).agg({'average_min_temp': 'mean', 'average_max_temp': 'mean'}).reset_index()
new_df['MonthIndex'] = pd.to_datetime(new_df['month'], format='%B', errors='coerce').dt.month
new_df = new_df.sort_values(by="MonthIndex")
# Preparing data
data = [
    go.Scatter(x=new_df['month'],
               y=new_df['average_max_temp'],
               text=new_df['month'],
               mode='markers',
               marker=dict(size=new_df['average_min_temp'],color=new_df['average_max_temp'], showscale=True))]

# Preparing layout
layout = go.Layout(title='Monthly Temps', xaxis_title="Month", yaxis_title="Temp", hovermode='closest')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechart.html')