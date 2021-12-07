import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv')
yes = df[df.Attrition == 'Yes']
education_data = {1: "Below College", 2: "College", 3: "Bachelor", 4: "Master", 5: "Doctor"}
education = yes.replace({"Education": education_data})
education['Education'].value_counts().plot(kind='pie', autopct='%.1f%%')
plt.show()

# OBSERVATION:
# DIFFERENT COLORS SHOWS DIFFERENT TYPES OF EMPLOYEES COMING TO A COMPANY
