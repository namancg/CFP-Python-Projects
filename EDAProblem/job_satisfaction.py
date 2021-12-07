import pandas as pd
import seaborn as seaborn
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
seaborn.countplot(x="JobSatisfaction", hue="Attrition", data=df)
plt.show()
