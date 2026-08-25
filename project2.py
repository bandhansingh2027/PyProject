import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

# print(data.head())
# print(data.columns)

highest = data.loc[data["No of Schools - Total"].idxmax()]
lowest = data.loc[data["No of Schools - Total"].idxmin()]

print("Highest number of schools:",highest)

print("\nLowest number of schools:",lowest)