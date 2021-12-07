import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
plt.figure(figsize=(8, 4))
plt.title('Environment Satisfaction')
plt.xlabel('Environment Satisfaction')
plt.ylabel('Number of Employees')
plt.hist(df.EnvironmentSatisfaction)
x = ["Low", "Medium", "High", "Very High"]
y = [1, 2, 3, 4]
plt.xticks(y, x)
plt.show()

# OBSERVATION:
# WHEN THE ENVIRONMENT SATISFACTION IS HIGH, THE NUMBER OF EMPLOYEES ARE HIGH
