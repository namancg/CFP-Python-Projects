import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

tips = sns.load_dataset("tips")
sns.swarmplot(x="day", y="total_bill", data=tips)

# giving title to the plot
plt.title('Graph')

# function to show plot
plt.show()
