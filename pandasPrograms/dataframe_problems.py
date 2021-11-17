"""
DATAFRAME PROGRAMS:
5: Write a Python program to create and display a DataFrame from a specified dictionary data which has the index
labels.
6. Write a Python program to display a summary of the basic information about a specified Data Frame and its data.
7. Write a Python program to get the first 3 rows of a given DataFrame. Sample Python dictionary data and list labels:
8. Write a Python program to select the 'name' and 'score' columns from the following DataFrame.
9. Write a Python program to select the specified columns and rows from a given data frame.
10. Write a Python program to select the rows where the number of attempts in the examination is greater than 2.
11. Write a Python program to count the number of rows and columns of a DataFrame. Sample data:
12. Write a Python program to select the rows where the score is missing, i.e. is NaN.
13. Write a Python program to select the rows where number of attempts in the examination is less than 2 and score
greater than 15.
14. Write a Python program to change the score in row 'd' to 11.5.
15. Write a Python program to calculate the sum of the examination attempts by the students.
16. Write a Python program to calculate the mean score for each different student in DataFrame.
17. Write a Python program to append a new row 'k' to data frame with given values for each column. Now delete the
new row and return the original DataFrame
18. Write a Python program to sort the DataFrame first by 'name' in descending order, then by 'score' in ascending
order.
19. Write a Python program to replace the 'qualify' column contains the values 'yes' and 'no' with True and False.
20. Write a Python program to delete the 'attempts' column from the DataFrame.
21. Write a Python program to insert a new column in existing DataFrame.
22. Write a Python program to iterate over rows in a DataFrame.
23. Write a Python program to get list from DataFrame column headers.
"""
import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# 5th Program
df = pd.DataFrame(exam_data, index=labels)
print(df)

# 6th Program
print("Summary of the basic information about this DataFrame and its data:")
print(df.info())

# 7th Program
print(df.iloc[:3])

# 8th Program
print("Select specific columns:")
print(df[['name', 'score']])

# 9th Program
print("Select specific columns and rows:")
print(df.iloc[[1, 3, 5, 6], [1, 3]])

# 10th Program
print("Number of attempts in the examination is greater than 2:")
print(df[df['attempts'] > 2])

# 11th Program
total_rows = len(df.axes[0])
total_cols = len(df.axes[1])
print("Number of Rows: " + str(total_rows))
print("Number of Columns: " + str(total_cols))

# 12th Program
print("Rows where score is missing:")
print(df[df['score'].isnull()])

# 13th Program
print("Number of attempts in the examination is less than 2 and score greater than 15 :")
print(df[(df['attempts'] < 2) & (df['score'] > 15)])

# 14th Program
print("Change the score in row 'd' to 11.5:")
df.loc['d', 'score'] = 11.5
print(df)

# 15th Program
print("Sum of the examination attempts by the students:")
print(df['attempts'].sum())

# 16th Program
print("Mean score for each different student in data frame:")
print(df['score'].mean())

# 17th Program
print("Append a new row:")
df.loc['k'] = [1, 'Suresh', 'yes', 15.5]
print("Print all records after insert a new record:")
print(df)
print("Delete the new row and display the original  rows:")
df = df.drop('k')
print(df)

# 18th Program
df.sort_values(by=['name', 'score'], ascending=[False, True])
print("Sort the data frame first by ‘name’ in descending order, then by ‘score’ in ascending order:")
print(df)

# 19th Program
print("Replace the 'qualify' column contains the values 'yes' and 'no'  with True and  False:")
df['qualify'] = df['qualify'].map({'yes': True, 'no': False})
print(df)

# 20th Program
print("Delete the 'attempts' column from the data frame:")
df.pop('attempts')
print(df)

# 21st Program
color = ['Red', 'Blue', 'Orange', 'Red', 'White', 'White', 'Blue', 'Green', 'Green', 'Red']
df['color'] = color
print("\nNew DataFrame after inserting the 'color' column")
print(df)

# 22nd Program
for index, row in df.iterrows():
    print(row['name'], row['qualify'])

# 23rd Program
print(list(df.columns.values))
