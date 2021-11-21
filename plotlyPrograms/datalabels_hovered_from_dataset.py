import plotly.graph_objects as go
import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv")
print(data.head())
fig = go.Figure(data=go.Scatter(x=data['Postal'],
                                y=data['Population'],
                                mode='markers',
                                marker_color=data['Population'],
                                text=data['State']))

fig.update_layout(title='Population of USA States')
fig.show()
