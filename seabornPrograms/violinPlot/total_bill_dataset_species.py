import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# use to set style of background of plot
sns.set(style="whitegrid")

# loading data-set inside a csv
data = pd.read_csv('iris.csv')
ax = sns.violinplot(x='species', y='sepal_length',data=data)

# giving title to the plot
plt.title('Graph')

# function to show plot
plt.show()
