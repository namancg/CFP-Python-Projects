import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
job_involvement = df["JobInvolvement"]
colors = ["red", "yellow", "green", "blue"]
plt.title("Job involvement")
x = ["Low", "Medium", "High", "Very High"]
plt.pie(df.JobInvolvement.value_counts(), colors=colors, labels=x, startangle=100, autopct='%1.1f%%')
plt.show()
