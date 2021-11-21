import plotly.express as px
import numpy as np

X = np.random.randn(1000)
Y = np.random.randn(1000)
fig = px.scatter(x=X, y=Y)
fig.show()
