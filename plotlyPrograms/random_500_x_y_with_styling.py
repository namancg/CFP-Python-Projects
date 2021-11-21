import plotly.express as px
import numpy as np
import random

X = np.random.randn(500)
Y = np.random.randn(500)
colors = [random.randint(1, 10) for i in range(500)]
fig = px.scatter(x=X, y=Y, color=colors)
fig.show()
