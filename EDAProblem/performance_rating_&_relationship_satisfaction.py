import seaborn as seaborn
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv')
fig, ax = plt.subplots(1, 2, figsize=(16, 4))
seaborn.distplot(df['PerformanceRating'], ax=ax[0])
seaborn.distplot(df['RelationshipSatisfaction'], ax=ax[1])
plt.show()

# OBSERVATION
# WHEN THE DENSITY OF THE EMPLOYEES IS MORE, PERFORMANCE INCREASES
# WHEN THE DENSITY OF THE EMPLOYEES IS MORE, RELATIONSHIP SATISFACTION INCREASES
