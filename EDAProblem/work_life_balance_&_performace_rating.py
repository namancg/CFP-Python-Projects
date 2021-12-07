import matplotlib.pyplot as plt
import pandas as pd
import seaborn as seaborn

df = pd.read_csv('data.csv')
f, axs = plt.subplots(1, 2, figsize=(14, 6))
seaborn.barplot(y="JobSatisfaction", x="PerformanceRating", hue="Attrition", data=df, ax=axs[0])
seaborn.barplot(y="WorkLifeBalance", x="PerformanceRating", hue="Attrition", data=df, ax=axs[1])
plt.show()

# OBSERVATIONS:
# WHEN JOB SATISFACTION IS YES, PERFORMANCE ALSO INCREASES
# WHEN JOB SATISFACTION IS NO, PERFORMANCE ALSO DECREASES
