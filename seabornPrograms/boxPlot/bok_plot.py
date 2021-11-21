import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gapminder = pd.read_csv(
    "https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv")
sns.boxplot(y='lifeExp', x='continent',
            data=gapminder,
            width=0.5,
            palette="colorblind")

# giving title to the plot
plt.title('Graph')

# function to show plot
plt.show()
