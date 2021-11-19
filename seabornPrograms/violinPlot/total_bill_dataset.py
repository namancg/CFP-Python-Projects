import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# use to set style of background of plot
sns.set(style="whitegrid")

# loading data-set inside a csv
data = pd.read_csv('data.csv')
ax = sns.violinplot(x='day', y='total_bill', data=data, hue='sex', split='True')

# giving title to the plot
plt.title('Graph')

# function to show plot
plt.show()
