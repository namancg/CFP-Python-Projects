import pandas as pd
import seaborn as seaborn
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
seaborn.countplot(x="YearsAtCompany", hue="Attrition", data=df)
plt.show()

# OBSERVATION:
# EMPLOYEES WHO HAVE WORKED FOR 1-4 YEARS ARE ATTRIED MORE THAN OTHERS
