import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", data=tips)

# giving title to the plot
plt.title('Graph')

# function to show plot
plt.show()
