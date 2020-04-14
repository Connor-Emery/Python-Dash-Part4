import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df3 = pd.read_csv('../Datasets/Olympic2016Rio.csv')
df4 = pd.read_csv('../Datasets/Weather2014-15.csv')

app = dash.Dash()

# Bubble chart
new_df = df4.groupby(['month']).agg({'average_min_temp': 'mean', 'average_max_temp': 'mean'}).reset_index()
new_df['MonthIndex'] = pd.to_datetime(new_df['month'], format='%B', errors='coerce').dt.month
new_df = new_df.sort_values(by="MonthIndex")
# Preparing data
data_bubblechart = [
    go.Scatter(x=new_df['month'],
               y=new_df['average_max_temp'],
               text=new_df['month'],
               mode='markers',
               marker=dict(size=new_df['average_min_temp'],color=new_df['average_max_temp'], showscale=True))]
# Layout
app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Bubble chart', style={'color': '#df1e56'}),
    dcc.Graph(id='graph6',
              figure={
                  'data': data_bubblechart,
                  'layout': go.Layout(title='Monthly Temps',
                                      xaxis={'title': 'Month'}, yaxis={'title': 'Temp'},
                                      hovermode='closest')
              }
              ),

])

if __name__ == '__main__':
    app.run_server()