import plotly.express as px
import numpy as np

X = np.random.randn(100)
Y = np.random.randn(100)
fig = px.scatter(x=X, y=Y)
fig.show()
