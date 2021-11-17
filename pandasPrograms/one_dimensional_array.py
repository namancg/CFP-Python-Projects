"""
PROGRAM 1 AND 2 - Write a Python program to create and display a one-dimensional array-like object
containing an array of data using Pandas module and converting Panda series to list
"""
import pandas as pd

ds = pd.Series([2, 4, 6, 8, 10])
print(ds)
print("Convert Pandas Series to Python list")
print("AT PRESENT TYPE IS: ", type(ds))

print(ds.tolist())
print("AFTER CONVERTING: ", type(ds.tolist()))
